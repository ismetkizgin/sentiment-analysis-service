from werkzeug.wrappers import Request, Response
import os

class ApiKeyVerify():
    def __init__(self, app):
          self.app = app

    def __call__(self, environ, start_response):
          request = Request(environ)
          if os.environ.get('API_KEY') is None or os.environ.get('API_KEY') == request.headers.get('x-api-key'):
               return self.app(environ, start_response)
          
          res = Response('Forbidden', mimetype='text/plain', status=403)
          return res(environ, start_response)