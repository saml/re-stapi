__author__ = 'saml'

from restapiexample import app

def test_index():
    client = app.test_client()
    assert(b'GET index' == client.get("/").data)
    assert(b'{}' == client.get("/", headers={'accept': 'application/json'}).data)
    assert(b'POST index' == client.post("/").data)