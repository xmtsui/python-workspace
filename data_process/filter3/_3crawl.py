#!/usr/bin/python
#-*- coding: utf-8 -*-
import string
file_read = open('data3.txt','r')
file_write = open('result3.txt', 'w')
file_read.seek(0,0)
line_temp = []

try:
  while True:
    #读取每一行数据，放在line_temp中
    line = file_read.readline()
    if len(line) == 0: # Zero length indicates EOF
      break
    line_temp.append(line)

  line_index = 0
  first_digit = []
  #遍历每一行数据，解析出出现的第一个数字
  for line_item in line_temp:
    i = 0
    #跳过第一个词
    while(line_item[i].isalpha()):
      i+=1

    #跳过中间的空格与tab
    while(line_item[i] == ' ' or line_item[i] == '	'):
      i+=1

    #开始组合第一个数字
    digit_combine = ''
    while(line_item[i] != '\r' or line_item[i] != '\n'):
      if(line_item[i].isdigit() or line_item[i] == '.'):
        digit_combine += line_item[i]
      elif(line_item[i] == '	' or line_item[i] == ' '):
	print digit_combine
        if(digit_combine == '0'):
	  print line_temp.pop(line_index)
	  digit_combine = ''
	else:
	  digit_combine = ''
      i+=1
    line_index+=1
  #写入结果文档
  for item in line_temp:
    file_write.write("%s" % item)
finally:
     file_read.close()
     file_write.close()
'''
    tmp = []
    if( line_index % 3 == 0):
      for index in range(1,4):
	#print 'number is:',
	#print first_digit[line_index-index]
	#print 'atof is:',
	#print string.atof( first_digit[line_index-index] )
	#if ( first_digit[line_index-index] == '\n' or first_digit[line_index-index] == '' or first_digit[line_index-index] == ' ' or first_digit[line_index-index] == '	'):
	#  continue
	try:
          if( string.atof( first_digit[line_index-index]) == 0 ):
	    line_temp.pop(line_index-index)
          elif( string.atof( first_digit[line_index-index] ) > 1000 ):
	    line_temp.pop(line_index-index)
	  else:
	    continue
	except ValueError,e:
	  print "error",e,"on line",line_index-index
'''
