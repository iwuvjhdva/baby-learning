#!/usr/bin/env python3

import cherrypy

from backend.db import db, init_database
from backend.application import Exercises


def cors():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"


def profile():
    cherrypy.request.profile = db.client.profiles.find_one({
        'user': 'linoy'
    })


if __name__ == '__main__':
    cherrypy.server.socket_host = '0.0.0.0'

    cherrypy.tools.cors = cherrypy.Tool('before_finalize', cors)
    cherrypy.tools.profile = cherrypy.Tool('on_start_resource', profile)

    cherrypy.config.update('server.conf')
    init_database()

    config = {'/': {
        'tools.cors.on': True,
        'tools.profile.on': True
    }}
    cherrypy.tree.mount(Exercises(), '/exercises', config)

    cherrypy.engine.start()
    cherrypy.engine.block()
