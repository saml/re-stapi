import json

from flask import request, Response, url_for, jsonify
from flask.views import MethodView


def asjson(resource):
    return Response(json.dumps(resource.repr_hal()), mimetype='application/json')

class Resource(object):
    dispatch = {}
    def method(self, method_name):

        self.dispatch[method_name][content_type][accept]
    def __call__(self, **args, **kwargs):
        pass

    def dispatch_request(self, *args, **kwargs):
        raise NotImplementedError()




class Index(MethodView):
    @resource.method('GET')
    @resource.content_type('application/json')
    @resource.accept('application/json')
    def get(self):
        return 'hello: ' + url_for('.index', _external=True)

    def post(self):
        return 'bye: ' + url_for('.index', _external=True)

def hello():
    return 'hello func ' + url_for('.hello', _external=True)

class ImageCollection(MethodView):
    def get(self):
        return jsonify([])
