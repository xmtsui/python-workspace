#!/usr/bin/python
# Filename : readfile.py

file_object = open('name.txt')
line_temp = []
t = []
try:
	while True:
		line = file_object.readline()
		if len(line) == 0: # Zero length indicates EOF
			break
		line_temp.append(line)
	for item in line_temp:
		t = item.split('	')
	for item in t:
		print item
finally:
     file_object.close( )
