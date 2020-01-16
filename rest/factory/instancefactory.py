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

import rest.api.tracks.tracks
import rest.api.albums.albums
import rest.api.images.images
import rest.api.sources.sources
import rest.api.urischemes.urischemes

class InstanceFactory:

    def __init__( self ):
        pass

    def getInstance( self, type ):
        """ Returns an instance based on the give type.
        Otherwise, it returns None.
        """

        return {
            'album'   : rest.api.albums.albums.Albums( ),
            'albums'  : rest.api.albums.albums.Albums( ),
            'image'   : rest.api.images.images.Images( ),
            'images'  : rest.api.images.images.Images( ),
            'source'  : rest.api.sources.sources.Sources( ),
            'sources' : rest.api.sources.sources.Sources( ),
            'track'   : rest.api.tracks.tracks.Tracks( ),
            'tracks'  : rest.api.tracks.tracks.Tracks( ),
            'scheme'  : rest.api.urischemes.urischemes.URISchemes( ),
            'schemes' : rest.api.urischemes.urischemes.URISchemes( ),
            'urischeme'  : rest.api.urischemes.urischemes.URISchemes( ),
            'urischemes' : rest.api.urischemes.urischemes.URISchemes( ),
        }.get( type, None ) # None is default if 'type' not found.

    def isInstanceAvailable( self, type ):
        """ Checks if an instance is available for the given type.
        If an instance is supported, it returns True.  Otherwise, it returns False.
        """

        return {
            'album'   : True,
            'albums'  : True,
            'image'   : True,
            'images'  : True,
            'source'  : True,
            'sources' : True,
            'track'   : True,
            'tracks'  : True,
            'scheme'  : True,
            'schemes' : True,
            'urischeme'  : True,
            'urischemes' : True,
        }.get( type, False ) # None is default if 'type' not found.
