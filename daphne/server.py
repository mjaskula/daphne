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

#Old endpoints

@app.route("/at_age/<age>")
def at_age(age=0):
  img_a = get_image(app.age_map_a, age)
  img_b = get_image(app.age_map_b, age)

  return '''
  <body>
    <table>
      <tr>
        <td>{}</td>
        <td>{}</td>
      </tr>
    </table>
  <body>
  '''.format(img_a, img_b)

@app.route("/test")
def test():
  return "<body><div style='width: 100%'><div style='width: 50%'><img src='/static/evelyn/IMG_0198.JPG'/></div><div style='width: 50%''><img src='/static/penelope/1008740_538649102860471_1196912_o.jpg'/></div></div><body>"

def get_image(age_map, age):
  l = age_map[age]
  if len(l) > 0:
    return "<img src='{}'/>".format(l[0])

  return "Not found"

if __name__ == '__main__':
  app.debug = True
  app.run()