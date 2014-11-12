from  collections import defaultdict
from datetime import datetime
import os

import exifread

def compare(birth_date_a, photo_dir_a, birth_date_b, photo_dir_b):
  agemap_a = age_map(birth_date_a, photo_dir_a)
  agemap_b = age_map(birth_date_b, photo_dir_b)
  for i in range(0, 400):
    print "{}: {}{}".format(i, '#' * len(agemap_a[i]), '*' * len(agemap_b[i]))

# map of age -> [photo paths]
def age_map(birth_date, photo_dir):
  m = defaultdict(list)
  for file_name in os.listdir(photo_dir):
    full_path = photo_dir  + os.sep + file_name
    photo_date = get_photo_date(full_path)
    if photo_date:
      age = (photo_date - birth_date).days
      m[age].append(full_path)
  return m

def get_photo_date(full_path):
  if full_path.endswith('.MOV'):
    return None
  
  tags = get_tags(full_path)
  datestr = None
  if 'Image DateTime' in tags:
    datestr = tags['Image DateTime'].values

  if not datestr:
    print "skipping {}: it has no date data".format(full_path)
    #TODO check for other date info/tags
    return 

  return datetime.strptime(datestr, "%Y:%m:%d %H:%M:%S")

def get_tags(file_name):
  with open(file_name, 'rb') as f:
     return exifread.process_file(f)

def main():
  compare(datetime(2011, 1,  6), '/Users/matthew/Documents/devel/daphne/daphne/static/evelyn',
      datetime(2013, 6, 15), '/Users/matthew/Documents/devel/daphne/daphne/static/penelope')

if __name__== '__main__':
  main()