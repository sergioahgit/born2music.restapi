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
import rest.api.apiinstancecontroller

if __name__ == '__main__':

    cherrypy.tree.mount(
        rest.api.apiinstancecontroller.APIInstanceController( "albums" ), '/albums',
        { '/' :
            { 'request.dispatch' : cherrypy.dispatch.MethodDispatcher( ) }
        }
    )

    cherrypy.tree.mount(
        rest.api.apiinstancecontroller.APIInstanceController( "urischemes" ), '/urischemes',
        { '/' :
            { 'request.dispatch' : cherrypy.dispatch.MethodDispatcher( ) }
        }
    )


    cherrypy.tree.mount(
        rest.api.apiinstancecontroller.APIInstanceController( "sources" ), '/sources',
        { '/' :
            { 'request.dispatch' : cherrypy.dispatch.MethodDispatcher( ) }
        }
    )
    
    cherrypy.tree.mount(
        rest.api.apiinstancecontroller.APIInstanceController( "images" ), '/images',
        { '/' :
            { 'request.dispatch' : cherrypy.dispatch.MethodDispatcher( ) }
        }
    )

    cherrypy.tree.mount(
        rest.api.apiinstancecontroller.APIInstanceController( "tracks" ), '/tracks',
        { '/' :
            { 'request.dispatch' : cherrypy.dispatch.MethodDispatcher( ) }
        }
    )

    cherrypy.config.update( {
        'tools.staticdir.debug': True,
        'log.screen': True,
        'server.socket_host' : '127.0.0.1',
        'server.socket_port' : 8080,
        'tools.sessions.on': True,
        'tools.encode.on': True,
        'tools.encode.encoding': 'utf-8'
    } )

    cherrypy.engine.start( )
    cherrypy.engine.block( )