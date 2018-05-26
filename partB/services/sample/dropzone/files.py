#!/usr/bin/env python3

import sys
import os

def main(directory):
  files = os.listdir(directory)	
  for file in files:
    print("{0}/{1}".format(directory, file))
		

try:
  main(sys.argv[1])
except:
  sys.exit(1)

sys.exit(0)
