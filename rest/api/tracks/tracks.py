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
from rest.api.entries.entries import Entries

# Global cache database table that holds the tracks entries
json_tracks_db = '''[
    {
        "id" : 1,
        "name" : "",
        "number" : 0,
        "size" : 174643,
        "artist" : 2,
        "album_name" : "",
        "territorial_availability" : "US",
        "available" : true,
        "duration_ms" : 10303,
        "explicit" : true,
        "popularity" : 100,
        "preview_source_id" : 2,
        "release_date" : "20190101",
        "source" : 2,
        "image" : 2,
        "artists" : [ 1 ],
        "albums" : [ 1 ],
        "images" : [ 1 ],
        "sources" : [ 1 ]
    }
]'''

class Tracks(Entries):

    def __init__( self ):

        # Load the json list that contains the track entries.
        super().__init__( json_tracks_db )

        # Define the required parameters for the track
        self.entry_required_params.append( [ "number", "album_name", "albums" ] )

    # Given the track 'id' it updates the track entry.
    def setEntry( self, json_data, id ):

        super( ).setEntry( json_data, id );