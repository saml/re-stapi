import os

from flask import Flask

app = Flask(__name__)
app.config.from_object('restapiexample.settings')
if os.environ.get('RESTAPI_SETTINGS_PATH') is not None:
    app.config.from_envvar('RESTAPI_SETTINGS_PATH')

from flask_restapi import route

from .resources import Index

route(app, '/', Index, 'index')