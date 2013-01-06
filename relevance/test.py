#!/usr/bin/python
# 
# filename: test.py
# author: tsui(tsui.uestc@gmail.com)
# date: 2013-01-05
#
import string

#Open files
name = "data"
last = ".txt"
filename = []
for index in range(1,18):
  tmpname = "%s%d%s" % (name,index,last)
  filename.append(tmpname)
for item in filename:
  print item
  file_data = open(item, 'w')
  file_data.close
