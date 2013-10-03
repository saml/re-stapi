__author__ = 'saml'

from flask_restapi import Resource
from restapiexample import mongo
from bson.json_util import dumps

from . import response_as

collection = Resource()

@collection.when(method='GET')
def get_authors():
    results = mongo.db.authors.find()
    return response_as(dumps(results))