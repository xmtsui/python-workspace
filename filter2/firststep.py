#!/usr/bin/python
#-*- coding: utf-8 -*-
import string
file_read = open('data.txt','r')
file_write = open('result_1step.txt', 'w')
file_read.seek(0,0)
line_temp = []
total_line = 0

try:
  while True:
    total_line += 1
    #读取每一行数据，放在line_temp中
    line = file_read.readline()
    if len(line) == 0: # Zero length indicates EOF
      break
    line_temp.append(line)

  line_index = 0
  #遍历每一行数据，解析出出现的第一个数字
  for line_index in range(0, total_line):
    print '!!!!!!!!!!!!!!'
    first_digit = 0
    second_digit = 0
    #原始数据
    #print line_temp[line_index]
    #print line_temp[line_index+1]

    #string 转化成 list
    #tmp1 = list(line_temp[line_index].split('\t'))
    tmp1 = list(line_temp[line_index])
    #tmp2 = list(line_temp[line_index+1].split('\t'))
    tmp2 = list(line_temp[line_index+1])
    #print tmp1
    #print tmp2

    #string 逆序
    tmp1.reverse()
    tmp2.reverse()
    rline_temp1 = ''.join(tmp1)
    rline_temp2 = ''.join(tmp2)
    print rline_temp1
    print rline_temp2

    print '-----------------'
    #1st
    digit_combine = ''
    for i in range(0, len(rline_temp1)):
      #跳过1,2词中间的空格与tab
      if(rline_temp1[i] == '\r' or rline_temp1[i] == '\n' or rline_temp1[i] == ' ' or rline_temp1[i] == '	'):
        continue
      #开始组合第一个数字
      if(rline_temp1[i].isdigit() or rline_temp1[i] == '.'):
        digit_combine += rline_temp1[i]
    try:
      #把第一个数字记录在first_digit里面
      print 'digit_combine'
      print digit_combine
      first_digit = string.atof(digit_combine)
    except ValueError,e:
      print "error",e,"on line",line_index

    #2nd
    digit_combine = ''
    for i in range(0, len(rline_temp2)):
      #跳过1,2词中间的空格与tab
      if(rline_temp1[i] == '\r' or rline_temp1[i] == '\n' or rline_temp1[i] == ' ' or rline_temp1[i] == '	'):
        continue
      #开始组合第一个数字
      if(rline_temp2[i].isdigit() or rline_temp2[i] == '.'):
        digit_combine += rline_temp2[i]
    try:	
      #把第一个数字记录在second_digit里面
      print 'digit_combine' 
      print digit_combine
      second_digit = string.atof(digit_combine)
    except ValueError,e:
      print "error",e,"on line",line_index+1

    if(first_digit > second_digit):
      print line_temp.pop(line_index)
    elif(first_digit < second_digit):
      print line_temp.pop(line_index+1)
    else:
      line_index+=2
      continue
    
    #下两个
    line_index+=2

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
