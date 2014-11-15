from pymongo import MongoClient

mongo_uri = 'mongodb://localhost:27017/'

db = MongoClient(mongo_uri).daphne
images = db.images
people = db.people


def write(person):
  for image in person['images']:
    _write_image(image)
  person.pop('images')
  _write_person(person)

def _write_image(image):
  print "writing {}".format(image.get('_id', None))
  images.insert(image)

def _write_person(person):
  people.insert(person)