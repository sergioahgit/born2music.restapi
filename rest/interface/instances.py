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
from abc import ABC, abstractmethod

class Instances(ABC):

    def __init__( self, json_entries_db ):

        self.entries_db = json.loads( json_entries_db )
        self.entry_required_params = [ ]

    # abstract method
    def setEntry( self, json_data, id ):
        pass

    def getEntry( self, id ):

        if id is None:
            raise cherrypy.HTTPError( HTTP_400_BAD_REQUEST_CODE, HTTP_400_BAD_REQUEST_MSG_MALFORMED_DATA )

        for entry in self.entries_db:

            if int( entry[ 'id' ] ) == int( id ):
                return entry

        raise cherrypy.HTTPError( HTTP_400_BAD_REQUEST_CODE, HTTP_400_BAD_REQUEST_MSG_MALFORMED_DATA )

    # Given the json_data list containing source entries, it updates the source entry in the database.
    def setEntries( self, json_data ):

        for entry in json_data:
            self.setEntry( entry, None )

    def getEntries( self ):

        return self.entries_db

    def getEntries( self, ids = None ):

        if ids is None:
            return self.entries_db
            #raise cherrypy.HTTPError( HTTP_400_BAD_REQUEST_CODE, HTTP_400_BAD_REQUEST_MSG_MALFORMED_DATA )

        entries = [ ]
        for id in ids:
            entries.append( self.getEntry( id ) )

        return entries