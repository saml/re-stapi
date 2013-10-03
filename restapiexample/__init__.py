import os

from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config.from_object('restapiexample.settings')
if os.environ.get('RESTAPI_SETTINGS_PATH') is not None:
    app.config.from_envvar('RESTAPI_SETTINGS_PATH')
mongo = PyMongo(app)

from flask_restapi import route

from .views import author

route(app, '/authors', author.collection, 'author_collection')