from flask import request, abort, Response

from .helpers import is_accept, is_method, is_mimetype, true

class Resource(object):
    def __init__(self):
        self.dispatch = []
        self.methods = set()

    def method(self, http_method):
        pred = is_method(http_method)
        self.methods.add(http_method)
        return self._if(pred)

    def accept(self, http_accept):
        return self._if(is_accept(http_accept))

    def mimetype(self, http_content_type):
        return self._if(is_mimetype(http_content_type))

    def anded(self, *preds):
        pass

    def when(self, method=None, accept=None, mimetype=None):
        if method is not None:
            self.methods.add(method)
            method_fn = is_method(method)
        else:
            method_fn = true

        accept_fn = is_accept(accept) if accept is not None else true
        mimetype_fn = is_mimetype(mimetype) if mimetype is not None else true
        
        pred = lambda: accept_fn() and method_fn() and mimetype_fn()
        return self._if(pred)

    def _if(self, pred):
        def wrapped(fn):
            self.dispatch.append((pred, fn))
            return fn
        return wrapped

    def as_view(self, endpoint):
        def fn(*args, **kwargs):
            for pred,f in self.dispatch:
                if pred():
                    return f(*args, **kwargs)
            resp = Response('Non Exhaustive Resource (endpoint={}, name={}): {} '.format(endpoint, self.__name__, request.url))
            resp.status_code = 500
            abort(resp)
        return fn

def route(app, rule, resource, endpoint, **options):
    view_func = resource.as_view(endpoint)
    methods = [method for method in resource.methods]
    app.add_url_rule(rule, view_func=view_func, methods=methods, endpoint=endpoint, **options)


