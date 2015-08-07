import pymongo
import cherrypy


class DB(dict):
    __getattr__ = dict.__getitem__


db = DB(client=None)


def init_database():
    db_config = cherrypy.config['database']
    db.client = pymongo.MongoClient(
        db_config['mongodb_uri'])[db_config['mongodb_name']]
