import os

from flask import Flask

app = Flask(__name__)
app.config.from_object('restapi.settings')
if os.environ.get('RESTAPI_SETTINGS_PATH') is not None:
    app.config.from_envvar('RESTAPI_SETTINGS_PATH')

from .resources import Index, hello, ImageCollection

def route(rule, view_func, endpoint=None, **options):
    if hasattr(view_func, 'as_view'):
        assert endpoint is not None, 'when using MethodView, must pass the view function name (endpoint)'
        view_func = view_func.as_view(endpoint)
    app.add_url_rule(rule, view_func=view_func, endpoint=endpoint,**options)


route('/', Index, 'index')
route('/hello', hello, 'hello', methods=['POST'])
route('/images', ImageCollection, 'image_collection')
#route('/images/<path:', ImagesCollection, 'images_collection')
