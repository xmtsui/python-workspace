#!/usr/bin/python
# encoding: UTF-8
import re
import string

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'\d{4}/\d{1,2}')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('2001/10')
if match: 
  # 使用Match获得分组信息
  print match.group()
  date = match.group()
  dateadd = date.split('/')
  print dateadd[0], dateadd[1]
  datenum = string.atoi(dateadd[1])
  print datenum+1
