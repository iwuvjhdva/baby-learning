#!/usr/bin/env python3

import os

import cherrypy

from backend.db import db, init_database
from backend.application import Exercises


def cors():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"


def profile():
    cherrypy.request.profile = db.client.profiles.find_one({
        'user': 'linoy'
    })


def initialize():
    cherrypy.tools.cors = cherrypy.Tool('before_finalize', cors)
    cherrypy.tools.profile = cherrypy.Tool('on_start_resource', profile)

    root_path = os.path.dirname(os.path.abspath(__file__))
    cherrypy.config.update(os.path.join(root_path, 'server.conf'))

    init_database()

    config = {'/': {
        'tools.cors.on': True,
        'tools.profile.on': True
    }}
    cherrypy.tree.mount(Exercises(), '/exercises', config)


def application(environ, start_response):
    initialize()
    return cherrypy.tree(environ, start_response)


if __name__ == '__main__':
    cherrypy.server.socket_host = '0.0.0.0'

    initialize()

    cherrypy.engine.start()
    cherrypy.engine.block()
