from flask import Flask, make_response
from extensions.restx_api import api
from flask_cors import CORS
from resources.healthid import ns_smartcard

app = Flask(__name__)
CORS(app, supports_credentials=True)
api.init_app(app)

api.add_namespace(ns_smartcard, path='/api/smartcard')


@app.after_request
def after_request(resp):
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp


if __name__ == "__main__":
    app.run(port=5000, debug=True)

