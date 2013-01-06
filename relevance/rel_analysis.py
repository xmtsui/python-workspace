#!/usr/bin/python
# 
# filename: crawl.py
# author: tsui(tsui.uestc@gmail.com)
# date: 2013-01-05
#
import string
import urllib2
from sgmllib import SGMLParser

#Open files
file_tic = open('ticker.txt')
file_data = open('data.txt')

#temp vars
line_tic = []
line_data = []
tic_tmp = []

#read ticker
try:
  while True:
    line = file_tic.readline()
    if len(line) == 0: # Zero length indicates EOF
      break
    line = line.replace('\r', '')
    line = line.replace('\n', '')
    line = line.strip()
    line_tic.append(line)
  #for item in line_tic:
  #  print item
finally:
  file_tic.close( )

#read data
try:
  while True:
    line = file_data.readline()
    if len(line) == 0: # Zero length indicates EOF
      break
    line = line.replace('\r', '')
    line = line.replace('\n', '')
    line = line.strip()
    line_data.append(line)

  #for item in line_data:
  #   print item
  #tic_tmp = line_data[0].split('	')
  #print tic_tmp[0]
  #print tic_tmp[1]

finally:
  file_data.close()
  file_tic.close()

for tic_item in line_tic:
  for data_item in line_data:
    tic_tmp = []
    tic_tmp = data_item.split('	')
    if(len(tic_tmp) == 2)
      continue
    if(tic_item == tic_tmp[0]):
      print data_item
