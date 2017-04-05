#! /usr/bin/python
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

