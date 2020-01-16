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

# Global cache database table that holds the source entries
json_sources_db = '''[
    {
        "id" : 1,
        "uri" : "https://www.linkedin.com",
        "scheme" : 6
    },
    {
        "id" : 2,
        "uri" : "http://www.linkedin.com/",
        "scheme" : 5
    }
]'''

class Sources(Instances):

    exposed = True # to let cherrypy know that we're exposing all methods in this one

    def __init__( self ):

        # Load the json list that contains the source entries.
        super( ).__init__( json_sources_db )

        # Define the required parameters for the sources
        self.entry_required_params.append( [ "id", "uri", "scheme" ] )

    # Given the source 'id' it updates the source entry.
    def setEntry( self, json_data, id ):

        # In order to make any type of edits, the 'id' is required.  Without the 'id', we cannot
        # edit or add a new entry.
        if id is None:

            if 'id' not in json_data:
                raise cherrypy.HTTPError( HTTP_400_BAD_REQUEST_CODE, HTTP_400_BAD_REQUEST_MSG_MALFORMED_DATA )

            id = json_data[ 'id' ]
            if id is None:
                raise cherrypy.HTTPError( HTTP_400_BAD_REQUEST_CODE, HTTP_400_BAD_REQUEST_MSG_MALFORMED_DATA )

        # Verify all required parameters.
        for param in self.entry_required_params:

            if param not in json_data:
                raise cherrypy.HTTPError( HTTP_400_BAD_REQUEST_CODE, HTTP_400_BAD_REQUEST_MSG_MALFORMED_DATA )

        # Let's modify the record for the given 'id'
        for entry in self.entries_db:

            if int( entry[ 'id'] ) == int( id ):

                entry[   'uri'  ] = json_data[ 'uri'  ]
                entry[ 'scheme' ] = json_data[ 'scheme' ]
                return

        # Otherwise, this will be a new record to add.  In this case, we will append the record.
        self.entries_db.append( {            
            "id" : id,
            "uri" : json_data[ 'uri' ],
            "scheme" : json_data[ 'scheme' ]
        } )