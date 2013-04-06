#!/usr/bin/python
#-*- coding: utf-8 -*-
import string
import re

#file operation
file_read = open('data.txt','r')
file_write = open('result.txt', 'w')
file_read.seek(0,0)
line_temp = []

#re definition
pattern = re.compile(r'\d{4}/\d{1,2}')
try:
  while True:
    #读取每一行数据，放在line_temp中
    line = file_read.readline()
    if len(line) == 0: # Zero length indicates EOF
      break
    line_temp.append(line)

  line_word = []
  #遍历每一行数据
  for line_item in line_temp:
    #print line_item
    i=0
    line_word = line_item.split('	')
    for word_item in line_word:
      #print word_item
      match = pattern.match(word_item)
      if match:
        # 使用Match获得分组信息
        #print match.group()
        date = match.group()
        date_split = date.split('/')
        #print date_split[0], date_split[1]
        year = date_split[0]
        month = string.atoi(date_split[1])
	if month == 12:
	  continue
	elif month == 11:
	  print '%s/%d	%s	%s' % (year, month, line_word[i+1], line_word[i+2])
	  print '%s/%d	%s	%s' % (year, month+1, line_word[i+1], line_word[i+2])
	else:  
	  #print 'year', year, 'month', month
	  #print 'year', year, 'month+1', month+1
	  #print '%s/%d' % (year, month+1)
          print '%s/%d	%s	%s' % (year, month, line_word[i+1], line_word[i+2])
          print '%s/%d	%s	%s' % (year, month+1, line_word[i+1], line_word[i+2])
          print '%s/%d	%s	%s' % (year, month+2, line_word[i+1], line_word[i+2])
          #print line_word[i+1], line_word[i+2] 
      i = i+1	
      
  #写入结果文档
  #for item in line_temp:
   # file_write.write("%s" % item)
finally:
     file_read.close()
     file_write.close()
