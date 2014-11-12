from flask import Flask
from datetime import datetime

import daphne

app = Flask("daphne")

@app.route("/load")
def load():
  app.age_map_a = daphne.age_map(datetime(2011, 1,  6), '/Users/matthew/Documents/devel/daphne/daphne/static/evelyn')
  app.age_map_b = daphne.age_map(datetime(2013, 6, 15), '/Users/matthew/Documents/devel/daphne/daphne/static/penelope')
  return "loaded"

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