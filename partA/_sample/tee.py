#!/usr/bin/env python3

# apply a regular expression to each incoming lines
# only print those that match

import sys

def main(filename):
  lines = sys.stdin.read()	
  lines = lines.split('\n')
  lines = [line for line in lines if len(line) > 0]


  with open(filename, 'w') as file:
    for line in lines:
      file.write(line)
      
      print(line)
    

try:
  main(sys.argv[1])
  
except:
  sys.exit(1)

sys.exit(0)