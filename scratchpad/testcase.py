from copy import deepcopy

class Request(object):
    def __init__(self, method=None, accept=None):
        self.method = method
        self.accept = accept
    def __str__(self):
        return 'Request({},{})'.format(self.method, self.accept)

#class PredicateBuilder(object):
#    def __init__(self):
#        self.preds = []
#
#    def method(self, http_method):
#        def pred(request):
#            return request.method == http_method
#        self.preds.append(p

class Resource(object):
    def __init__(self):
        self.dispatch = []
        self.preds = [] # current predicate being built.

    def method(self, http_method):
        def pred(request):
            return request.method == http_method
        def wrapped(fn):
            self.preds.append(pred)
            return fn
        return wrapped

    def accept(self, http_accept):
        def pred(request):
            return request.accept == http_accept
        def wrapped(fn):
            self.preds.append(pred)
            return fn
        return wrapped

    def done(self):
        print('done', self.preds)
        preds = self.preds#[pred for pred in self.preds]
        self.preds = []
        print('before', preds)
        def pred(request):
            print('after', preds)
            for predicate in preds:
                if not predicate(request):
                    return False
            return True

        def wrapped(fn):
            self.dispatch.append((pred, fn))
            return fn

        return wrapped


    def handle(self, request):
        for pred,fn in self.dispatch:
            if pred(request):
                fn()
                return True
        return False
        


Index = Resource()

@Index.method('GET')
@Index.accept('applicaiton/json')
@Index.done()
def g():
    print('g')

@Index.method('GET')
@Index.done()
def f():
    print('f')


class Server(object):
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def handle(self, request):
        for handler in self.handlers:
            result = handler.handle(request)
            if result:
                return
        print("can't handle: {}".format(request))

server = Server()
server.add_handler(Index)
server.handle(Request('GET'))  # f
server.handle(Request('GET', 'application/json')) # g

