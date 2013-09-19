
class Resource(object):
    def render_GET(self, request):
        raise NotImplementedError('Resource is abstract. Derive this and implement.')
    def render_PUT(self, request):
        raise NotImplementedError('Resource is abstract. Derive this and implement.')
    def render_DELETE(self, request):
        raise NotImplementedError('Resource is abstract. Derive this and implement.')
    def render_POST(self, request):
        raise NotImplementedError('Resource is abstract. Derive this and implement.')

class WorkspaceResource(Resource):
    def repr_hal(self, request):
        pass

resources = None
        
