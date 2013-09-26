from flask import jsonify

from flask_restapi import Resource

Index = Resource()

@Index.when(method='GET')
def index():
    return 'GET index'

@Index.method('POST')
def index_post():
    return 'POST index'

#@Index.anded(Index.method('GET'), Index.accept('application/json'))
@Index.method('GET')
@Index.accept('application/json')
def index_get_json():
    return jsonify()