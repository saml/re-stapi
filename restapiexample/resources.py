from flask import jsonify

from flask_restapi import Resource

Index = Resource()


@Index.method('GET')
def index():
    return 'GET index'

@Index.method('POST')
def index_post():
    return 'POST index'

@Index.when(method='GET', accept='application/json')
def index_get_json():
    return jsonify()
