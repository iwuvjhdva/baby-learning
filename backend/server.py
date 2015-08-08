#!/usr/bin/env python3

import cherrypy

from backend.db import init_database
from backend.application import Exercises


def cors():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"


if __name__ == '__main__':
    cherrypy.tools.cors = cherrypy.Tool('before_finalize', cors)
    cherrypy.config.update("server.conf")

    init_database()
    cherrypy.tree.mount(Exercises(), '/exercises', {'/': {'tools.cors.on': True}})

    cherrypy.engine.start()
    cherrypy.engine.block()
