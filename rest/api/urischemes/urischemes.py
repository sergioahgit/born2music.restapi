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
import rest.common.errorcodes
from rest.interface.instances import Instances

# Global cache database table that holds the urischeme entries
json_urischemes_db = '''[
    {
        "id" : 1,
        "type" : "chrome",
        "purpose" : "Specifies user interfaces built using XUL in Mozilla-based browsers."
    },
    {
        "id" : 2,
        "type" : "file",
        "purpose" : "Addressing files on local or network file systems."
    },
    {
        "id" : 3,
        "type" : "ftp",
        "purpose" : "FTP Resources."
    },
    {
        "id" : 4,
        "type" : "git",
        "purpose" : "Provides a link to a GIT repository."
    },
    {
        "id" : 5,
        "type" : "http",
        "purpose" : "HTTP Resources."
    },
    {
        "id" : 6,
        "type" : "https",
        "purpose" : "Secured HTTP connections using SSL/TLS."
    }
]'''

#
#### `/scheme`
#```
#GET    retrieve list of all schemes
#
#    Response
#    200    JSON array with list of all schemes
#    404    The specified resource does not exist.
#
#POST
#
#    Payload:
#    JSON dictionary or array with scheme details, if 'id' is provided then edit.
#
#    {
#        "id" : unique id,
#        "scheme" : scheme string (defined by the Official IANA-registered schemes).
#        "purpose" : The purpose of the scheme
#    }
#
#    Response:
#    200    Ok
#    400    Data in the body is malformed.
#```

class URISchemes(Instances):

    def __init__( self ):

        # Load the json list that contains the scheme entries.
        super( ).__init__( json_urischemes_db )

        # Define the required parameters for the scheme
        self.entry_required_params.append( [ "id", "type", "purpose" ] )

    # Given the scheme 'id' it updates the scheme entry.
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

                entry[   'type'  ] = json_data[ 'type'  ]
                entry[ 'purpose' ] = json_data[ 'purpose' ]
                return

        # Otherwise, this will be a new record to add.  In this case, we will append the record.
        self.entries_db.append( {            
            "id" : id,
            "type" : json_data[ 'type' ],
            "purpose" : json_data[ 'purpose' ]
        } )