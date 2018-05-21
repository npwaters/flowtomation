#!/usr/bin/env python3

# apply a regular expression to each incoming lines
# only print those that match

import sys
import re

def main(regex):
  lines = sys.stdin.read()	
  lines = lines.split('\n')
  lines = [line for line in lines if len(line) > 0]


  for line in lines:
    if re.search(regex, line):
      print(line)	


try:
  main(sys.argv[1])
  
except:
  sys.exit(1)

sys.exit(0)