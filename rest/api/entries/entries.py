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
from rest.interface.instances import Instances

class Entries(Instances):

    def __init__( self, json_entries_db ):

        super( ).__init__( json_entries_db )
        self.entry_required_params = [ "name", "size", "artist_id", "territorial_availability", "available", "duration_ms", "explicit", "popularity", "preview_source_id" ]

    def setEntry( self, json_data, id ):

        if id is None:

            if 'id' not in json_data:
                raise cherrypy.HTTPError( 400, "Malformed Request - 'id' not specified." )

            id = json_data[ 'id' ]
            if id is None:
                raise cherrypy.HTTPError( 400, "Malformed Request - 'id' no specified." )

        for param in self.entry_required_params:

            if param not in json_data:
                raise cherrypy.HTTPError( 400, "Malformed Request - '%s' not specified." % (param) )

        for entry in self.entries_db:

            if int( entry[ 'id'] ) == int( id ):

                entry[                     'name' ] = json_data[ 'name'  ]
                entry[                     'size' ] = json_data[ 'size' ]
                entry[                    'artist'] = json_data[ 'artist' ]
                entry[ 'territorial_availability' ] = json_data[ 'territorial_availability' ]
                entry[                'available' ] = json_data[ 'available' ]
                entry[              'duration_ms' ] = json_data[ 'duration_ms' ]
                entry[                 'explicit' ] = json_data[ 'explicit' ]
                entry[               'popularity' ] = json_data[ 'popularity' ]
                entry[           'preview_source' ] = json_data[ 'preview_source' ]
                return

        self.entries_db.append( {            
            "id" : id,
            "size" : json_data[ 'size' ],
            "artist_id" : json_data[ 'artist_id' ],
            "territorial_availability" : json_data[ 'territorial_availability' ],
            "available" : json_data[ 'available' ],
            "duration_ms" : json_data[ 'duration_ms' ],
            "explicit" : json_data[ 'explicit' ],
            "popularity" : json_data[ 'popularity' ],
            "preview_source_id" : json_data[ 'preview_source_id' ]
        } )