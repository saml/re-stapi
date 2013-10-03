__author__ = 'saml'

from flask import make_response

def response_as(body_str, mimetype='application/json', charset='utf-8'):
    resp = make_response(body_str)
    content_type = '{0}; charset={1}'.format(mimetype, charset)
    resp.headers['Content-Type'] = content_type
    return resp

