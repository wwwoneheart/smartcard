from flask import Flask
from extensions.restx_api import api
from resources.healthid import ns_smartcard

app = Flask(__name__)
api.init_app(app)

api.add_namespace(ns_smartcard, path='/smartcard')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
