#!/usr/bin/env python3.7

# The MIT License (MIT)
#
# Copyright (c) 2019-2020 Sergio A. Hernandez, Jr.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Except as contained in this notice, the name(s) of the above copyright holders shall not be used in
# advertising or otherwise to promote the sale, use or other dealings in this Software without prior
# written authorization.

import cherrypy
import json
from rest.common.util.jsonutil import getJSON
from rest.factory.instancefactory import InstanceFactory

class APIInstanceController:

    exposed = True # to let cherrypy know that we're exposing all methods in this one

    def __init__( self, type ):

        # /* --- Factory in charge of initializing the supported instances supported by the rest interface. --- */
        self.instanceFactory = InstanceFactory( )

        # /* --- Based on the given type, a corresponding instance class will be initialized. --- */
        self.instance = self.instanceFactory.getInstance( type )

        # /* --- Return the current entries stored by the instance. --- */
        self.entries_db = self.instance.getEntries( )

    def GET( self, *args, **kwargs ):
        """CherryPy passes all GET and POST variables as method parameters.
        It doesn't make a difference where the variables come from or how
        large their contents are.
        """

        cherrypy.response.headers[ 'content-type' ] = 'application/json'
        cherrypy.response.headers[ 'access-control-allow-origin' ] = '*'

        # /* --- When API -> /albums - We will dump the whole list. --- */
        if 'id' not in kwargs:
            return json.dumps( self.entries_db ).encode( 'utf8' )

        id = kwargs[ 'id' ]
        if not id.isdigit( ): # We will raise an error is we did not find the resource.
            raise cherrypy.HTTPError( HTTP_404_NOT_FOUND_CODE, HTTP_404_NOT_FOUND_MSG_RESOURCE_NOT_FOUND )

        # /* --- When API -> /<instance>/<id>/<...>/<...>/... - We will dump the corresponding value for the given type(parameter). --- */
        if len( args ) > 1:

            jsonvalue = self.entries_db
            for type in args[ 1:]:

                if type.isdigit( ):
                    jsonvalue = getJSON( type, None, instance, jsonvalue )

                else:
                    instance = self.instanceFactory.getInstance( type )
                    if instance is None:

                        if isinstance( jsonvalue, list ):

                            jsonvalue = getJSON( id, type, instance, jsonvalue )
                            break;

                        return json.dumps( jsonvalue[ type ] ).encode( 'utf8' )

                    jsonvalue = getJSON( id, type, instance, jsonvalue )
            
            return json.dumps( jsonvalue ).encode( 'utf8' )

        # /* --- When API -> /albums/<id> - We will dump the corresponding entry. --- */
        for entry in self.entries_db:
            if int( id ) == int( entry[ 'id'] ):
                return json.dumps( entry ).encode( 'utf8' )

        # /* --- We will raise an error is we did not find the resource. --- */
        raise cherrypy.HTTPError( HTTP_404_NOT_FOUND_CODE, HTTP_404_NOT_FOUND_MSG_RESOURCE_NOT_FOUND )

    def POST( self, *args, **kwargs ):
        """CherryPy passes all GET and POST variables as method parameters.
        It doesn't make a difference where the variables come from or how
        large their contents are.
        The POST hasn't been implemented, yet.  This is just a pseudo code.
        """

        if 'Content-Length' not in cherrypy.request.headers:
            raise cherrypy.HTTPError( HTTP_411_LENGTH_REQUIRED_CODE, HTTP_411_LENGTH_REQUIRED_MSG_MISSING_CONTENT_LENGHT_HEADER )

        length = cherrypy.request.headers[ 'Content-Length' ]
        if 0 == length:
            raise cherrypy.HTTPError( HTTP_411_LENGTH_REQUIRED_CODE, HTTP_411_LENGTH_REQUIRED_MSG_CONTENT_LENGHT_IS_ZERO )

        body = cherrypy.request.body.read( length )
        json_data = json.loads( body )

        if 'id' not in kwargs:

            if isinstance( json_data, list ):
                return self.setEntries( json_data )

            return self.setEntry( json_data, None )

        raise cherrypy.HTTPError( HTTP_404_NOT_FOUND_CODE, HTTP_404_NOT_FOUND_MSG_RESOURCE_NOT_FOUND )

    def index( self, id=None ):
        """The index hasn't been implemented, yet.  This is just a pseudo code.
        """

        return "APIInstanceManager:index( ) not implemented."

    def _cp_dispatch( self, vpath ):
        """_cp_dispatch is a special method you declare in any of your controller
        to massage the remaining segments before CherryPy gets to process them.
        This offers you the capacity to remove, add or otherwise handle any segment
        you wish and, even, entirely change the remaining parts.
        """

        if vpath:

            cherrypy.request.params[ 'id' ] = vpath.pop( 0 )
            length = len( vpath )
            if length > 0:

                param = vpath[ 0 ]
                if self.instanceFactory.isInstanceAvailable( param ):
                    
                    params = [ ]
                    for i in range( length ):
                        params.append( vpath.pop( 0 ) )
                    
                    cherrypy.request.params[ 'params' ] = params
                    return

        if vpath:
            return getattr( self, vpath[ 0 ], None )