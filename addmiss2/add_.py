#!/usr/bin/python
#-*- coding: utf-8 -*-
import string
import re

#file operation
#file_read = open('data.txt','r')
#file_read = open('so1.txt','r')
file_read = open('so2.txt','r')
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
  line_word1 = []
  line_word2 = []
  i = -1
  cycle = 0
  #遍历每一行数据
  for line_item in line_temp:
    i = i + 1
    line_word = line_temp[i].split('	')
    if cycle == 0:
      #print line_item
      if(line_word[2] != "\r\n"):
        print "%s	%s	%s" % (line_word[0], line_word[1], line_word[2])
        line_word1 = line_temp[i+1].split('	')
        line_word2 = line_temp[i+2].split('	')
        print "%s	%s	%s" % (line_word1[0], line_word1[1], line_word[2])
        print "%s	%s	%s" % (line_word2[0], line_word2[1], line_word[2])
        cycle = 1	
    elif cycle == 1:
      cycle = 2 
      continue
    elif cycle == 2:
      cycle = 0
      continue
    else:
      print "error"
    
    #print len(line_word), line_word[2]
    #for word_item in line_word[2]:
    #  print ord(word_item)
    #'%d' % word_item
    #if(line_word[2] == "\r\n"):
    #  print "yes"
    #if(line_word[2] == "\r"):
    #  print "heheheh"
finally:
     file_read.close()
     file_write.close()
