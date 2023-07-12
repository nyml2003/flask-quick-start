from flask import Flask
from flask_cors import CORS
from gevent import pywsgi

from test import test as test_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(test_blueprint, url_prefix='/test')

server = pywsgi.WSGIServer(('0.0.0.0', 8090), app)
server.serve_forever()
