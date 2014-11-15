from  collections import defaultdict
from datetime import datetime
from itertools import ifilter
import logging as log
import os

import plistlib

#map of face_key -> {face_data, list of image_data}
def load_people(album_data_file=os.environ['HOME'] + '/Pictures/iPhoto Library/AlbumData.xml'):
  people = build_people_map(load(album_data_file))
  print("Loaded {} people".format(len(people)))
  return people

def load(album_data_file):
  print("Loading {}".format(album_data_file))
  album_data = plistlib.readPlist(album_data_file)
  print("Loaded {}".format(album_data_file))
  return album_data

#map of face_key -> {face_data, list of image_data}
def build_people_map(album_data):
  people_map = face_data(album_data)

  decorate_with_photos(people_map, album_data)

  return people_map

#map of face_key -> {face_data}
def face_data(album_data):
  # return {data['name']:data for id, data in album_data['List of Faces'].iteritems()}
  faces = album_data['List of Faces']
  for face in faces.values():
    # print "{} - {} - {}".format(face['key'], face['PhotoCount'], face['name'])
    face['images'] = []
  return faces

def decorate_with_photos(people_map, album_data):
  for image in images_with_faces(album_data):
    image['date'] = timestamp_to_date(image['DateAsTimerInterval'])
    for face in image['Faces']:
      people_map[face['face key']]['images'].append(image)

def images_with_faces(album_data):
  return ifilter(lambda img: 'Faces' in img, album_data['Master Image List'].values())


APPLE_EPOCH = datetime(2001, 1, 1)
POSIX_EPOCH = datetime(1970, 1, 1)
APPLE_OFFSET = (APPLE_EPOCH - POSIX_EPOCH).total_seconds()

def timestamp_to_date(timestamp):
  return datetime.fromtimestamp(APPLE_OFFSET + timestamp)

# map of age -> [photo paths]
def age_map(person, birthday):
  m = defaultdict(list)
  for image in person['images']:
    image_date = image['date']
    age = (image['date'] - birthday).days
    m[age].append(image)
  person.pop('images')
  return m

