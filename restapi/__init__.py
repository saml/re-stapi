import os

from flask import Flask

app = Flask(__name__)
app.config.from_object('restapi.settings')
if os.environ.get('RESTAPI_SETTINGS_PATH') is not None:
    app.config.from_envvar('RESTAPI_SETTINGS_PATH')

from .views import Index

def route(rule, method_view, endpoint, **options):
    app.add_url_rule(rule, view_func=method_view.as_view(endpoint), **options)

route('/', Index, 'index')
