import logging as log
from itertools import ifilter

import plistlib

def load_people_from_album_data_file(album_data_file):
  return build_people_map(load(album_data_file))

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
    print "{} - {} - {}".format(face['key'], face['PhotoCount'], face['name'])
    face['images'] = []
  return faces

def decorate_with_photos(people_map, album_data):
  for image in images_with_faces(album_data):
    for face in image['Faces']:
      people_map[face['face key']]['images'].append(image)

def images_with_faces(album_data):
  return ifilter(lambda img: 'Faces' in img, album_data['Master Image List'].values())


APPLE_EPOCH = datetime(2001, 1, 1)
POSIX_EPOCH = datetime(1970, 1, 1)
APPLE_OFFSET = (apple_epoch - posix_epoch).total_seconds()

def timestamp_to_date(timestamp):
  return datetime.fromtimestamp(APPLE_OFFSET + timestamp)