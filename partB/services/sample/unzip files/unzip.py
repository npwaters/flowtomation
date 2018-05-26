#!/usr/bin/env python3

# open up zip files...


import sys
import zipfile

def main():
	lines = sys.stdin.read()	
	lines = lines.split('\n')
	lines = [line for line in lines if len(line) > 0]

	for file in lines:
		if zipfile.is_zipfile(file):
			with zipfile.ZipFile(file) as myzip:
				for name in myzip.namelist():
					print(name)

main()

#try:
#	main()
#	
#except:
#	sys.exit(1)
#
#sys.exit(0)