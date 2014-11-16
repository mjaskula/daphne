from datetime import datetime

from flask import Flask, make_response, jsonify, Response 
from bson import json_util

import mongo as db

app = Flask("daphne")

@app.route('/')
def index():
  return make_response(open('templates/index.html').read())

@app.route('/people.json')
def people():
  return Response(
    json_util.dumps(db.people()),
    mimetype='application/json'
  )

if __name__ == '__main__':
  app.debug = True
  app.run()