#!/usr/bin/env python3

import cherrypy

from backend.db import init_database
from backend.exercises import Exercises

if __name__ == '__main__':
    cherrypy.config.update("server.conf")

    init_database()
    cherrypy.tree.mount(Exercises(), '/exercises')

    cherrypy.engine.start()
    cherrypy.engine.block()
