#!/usr/bin/env python3

import cherrypy

db_config = cherrypy.request.app.config['database']

db = pymongo.MongoClient(db_config['mongodb_uri'])[db_config['mongodb_name']]

states = {
    'step_1': None
}


class Exercises:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def next(self):
        profile = db.profiles.find_one({
            'user': 'linoy'
        })
        if profile['last_exercised'] < 0:
            pass
        return {}


if __name__ == '__main__':
    cherrypy.config.update("server.conf")
    cherrypy.tree.mount(Exercises(), '/exercises')

    cherrypy.engine.start()
    cherrypy.engine.block()
