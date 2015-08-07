#!/usr/bin/env python3

import cherrypy

from backend.exercises import Exercises

if __name__ == '__main__':
    cherrypy.config.update("server.conf")
    cherrypy.tree.mount(Exercises(), '/exercises')

    cherrypy.engine.start()
    cherrypy.engine.block()
