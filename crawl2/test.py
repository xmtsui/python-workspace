#!/usr/bin/python
# 
# filename: test.py
# author: tsui(tsui.uestc@gmail.com)
# date: 2013-01-05
#
page_index = 1
for page_index in range(1,4):
  re = 66 * page_index
  page_index_tmp = '%d' % re
  print 'd' +  page_index_tmp
  page_index+=1
