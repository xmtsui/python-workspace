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
line_tic = []
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

data = "data"
result = "result"
last = ".txt"
dataname = []
resultname = []
for index in range(1,18):
  tmp_data_name = "%s%d%s" % (data,index,last)
  tmp_result_name = "%s%d%s" % (result,index,last)
  dataname.append(tmp_data_name)
  resultname.append(tmp_result_name)
i = 0
for data_name_item in dataname:
  #print data_name_item
  #print i
  #print resultname[i]
  #i+=1
  file_data = open(data_name_item)
  file_result = open(resultname[i],'w')
  #temp vars
  line_data = []
  tic_tmp = []

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

    for tic_item in line_tic:
      for data_item in line_data:
        tic_tmp = []
        tic_tmp = data_item.split('	')
        if(len(tic_tmp) == 2):
          continue
        if(tic_item == tic_tmp[0]):
          print data_item
	  file_result.write("%s\r\n" % data_item)
  finally:
    file_data.close()
    file_result.close()

  #result index plus 1
  i+=1
