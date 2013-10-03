__author__ = 'saml'

from flask import make_response
from flask_restapi import Resource
from restapiexample import mongo
from bson.json_util import dumps

collection = Resource()

@collection.when(method='GET')
def get_authors():
    resp = make_response(dumps(mongo.db.authors.find()))
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp