from pymongo import MongoClient, ASCENDING

mongo_uri = 'mongodb://localhost:27017/'

db = MongoClient(mongo_uri).daphne
images = db.images
images.create_index([('key', ASCENDING), 
                    ('ImagePath', ASCENDING)], 
                    unique=True)
images.create_index([('age', ASCENDING)])
people = db.people
people.create_index('key', unique=True)


def write(person):
  for image in person['images']:
    _write_image(image)
  person.pop('images')
  _write_person(person)

def _write_image(image):
  images.update({'key': image['key'], 'ImagePath': image['ImagePath']}, 
                 image, 
                 upsert=True)

def _write_person(person):
  people.update({'key': person['key']}, person, upsert=True)