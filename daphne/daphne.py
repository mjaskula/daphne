from  collections import defaultdict
from datetime import datetime
import os

import exifread

def age_map(birth_date, photo_dir):
	m = defaultdict(list)
	for file_name in os.listdir(photo_dir):
		photo_date = get_photo_date(photo_dir, file_name)
		if photo_date:
			age = (photo_date - birth_date).days
			m[age].append(file_name)
	return m

def get_photo_date(dir, file_name):
	if file_name.endswith('.MOV'):
		return None
	
	tags = get_tags(dir  + os.sep + file_name)
	datestr = None
	if 'Image DateTime' in tags:
		datestr = tags['Image DateTime'].values

	if not datestr:
		print "skipping {}: it has no date data".format(file_name)
		return 

	return datetime.strptime(datestr, "%Y:%m:%d %H:%M:%S")

def get_tags(file_name):
	with open(file_name, 'rb') as f:
	 	return exifread.process_file(f)

def main():
	agemap = age_map(datetime(2011, 1, 6), '/Users/matthew/Pictures/evelyn')
	for i in range(0, 400):
		print "{}: {}".format(i, '#' * len(agemap[i]))

if __name__== '__main__':
	main()