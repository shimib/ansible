#! /usr/bin/python
from ansible.module_utils.basic import *
import json

def set_max_files(namesString, check_mode):
  filenames = namesString.split(",")
  files = map(lambda f: open(f, 'r') , filenames) 
  values = map(lambda f: f.readline(), files)
  numbers = map(lambda s: int(s), values)
  map(lambda f: f.close() , files) 
  maxNum = max(numbers)
  zipped = zip(numbers, filenames) 
  filtered = filter(lambda x: x[0] != maxNum, zipped)
  fileNamesToChange = map(lambda x: x[1], filtered)
  if not check_mode:
    files = map(lambda f: open(f, 'w') , fileNamesToChange) 
    map(lambda f: f.write(str(maxNum)), files)
    map(lambda f: f.close() , files) 
  
  return len(fileNamesToChange) > 0

def main():
 arg_spec = dict(
    files = dict(requires=True)
 ) 
 module = AnsibleModule(argument_spec = arg_spec, supports_check_mode = True)

 changed = set_max_files(module.params['files'], module.check_mode)

 module.exit_json(changed = changed)

if __name__ == '__main__': 
	main()
 
