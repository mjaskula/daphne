from __future__ import print_function
from datetime import datetime
import json

import iphoto

def yes_no(input):
  return input == 'y' or input == 'Y'

def ask_use(name):
  return ask("Use {}? (y/N) ".format(name), yes_no)

def birthday(input):
  return datetime.strptime(input, "%Y-%m-%d")

def ask_birthday(name):
  return ask("What is {}'s birthday? (yyyy-mm-dd) ".format(name), birthday)

def ask(question, answer_conversion):
  while True:
    try:
        return answer_conversion(raw_input(question))
    except ValueError:
        print("  Sorry, I didn't understand that.")
        continue

def write(data, file_name):
  with open(file_name, 'wb') as f:
    json.dump(data, f, indent=2, cls=DateTimeEncoder)

class DateTimeEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, datetime):
      return obj.isoformat()#TODO: timestamp?
    # Let the base class default method raise the TypeError
    return json.JSONEncoder.default(self, obj)

def main():
  people = iphoto.load_people()
  size = len(people)
  for i,(key,person) in enumerate(people.items()):
    print("({}/{}) ".format(i, size), end='')
    if ask_use(person['name']):
      birthday = ask_birthday(person['name'])
      person['age_map'] = iphoto.age_map(person, birthday)
    else:
      people.pop(key)
  write(people, "daphne_data.json")


if __name__== '__main__':
  main()