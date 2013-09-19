import json

from flask import request, Response, url_for
from flask.views import MethodView


def asjson(resource):
    return Response(json.dumps(resource.repr_hal()), mimetype='application/json')

class Index(MethodView):
    def get(self):
        return 'hello: ' + url_for('.index', _external=True)

    def post(self):
        return 'bye: ' + url_for('.index', _external=True)

def hello():
    return 'hello func ' + url_for('.hello', _external=True)
