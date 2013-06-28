#!/usr/bin/python
# coding=utf-8
# Filename : crawl.py
import urllib2
import codecs
from sgmllib import SGMLParser
from xml.sax.handler import ContentHandler  
from xml.sax import parse

import sys
reload(sys) 
sys.setdefaultencoding('utf-8')  
 
file_read = open('date.txt','r')
file_read.seek(0,0)
line_temp = []

class TestHandle(ContentHandler):
    static = 0
    circle = 0
    first = ""
    new = ""
    flag = 0
    def __init__(self):
        self.i = 0
    def startElement(self,name,attrs):
        # print 'name:',name, 'attrs:',attrs.keys()
        self.i
        if name == "instrumentId":
          TestHandle.flag = 1
        else:
          TestHandle.flag = 0
    def endElement(self,name):
        # print 'endname',name
        self.i
    def characters(self,chars):
        # print 'chars',chars
        if TestHandle.flag == 1 and TestHandle.static == 0:
          TestHandle.first = chars
          TestHandle.static = 1
        if TestHandle.flag == 1 and TestHandle.first == chars:
          TestHandle.circle=9
        if TestHandle.flag == 1 and TestHandle.first != chars:
          TestHandle.circle=0

        TestHandle.flag = 0
        chars = chars.strip().replace("\r\n", '')
        if self.i < TestHandle.circle:
        	if len(chars):
        		print chars, '	',
        		self.i = self.i+1
        else:
          if(self.i == TestHandle.circle and self.i != 0):
            TestHandle.static=0
            print
          self.i = 0

try:
  while True:
    line = file_read.readline()
    if len(line) == 0: # Zero length indicates EOF
      break
    line_temp.append(line)
  if __name__ == '__main__':
    # url = 'http://www.cffex.com.cn/fzjy/ccpm/201303/13/index.xml'
    for n in line_temp:
      file_write = open('index.xml', 'w')
      file_write.seek(0,0)
      n = n.replace("\r\n",'')
      # n = n.replace("\r\n",'')
      n_tmp = n.split('-')
      date = n_tmp[0] + n_tmp[1] + '/' + n_tmp[2]
      url = 'http://www.cffex.com.cn/fzjy/ccpm/' + date + '/index.xml'
      content = urllib2.urlopen(url).read()
      content = content.decode('gbk').encode('UTF-8')
      content = content.replace('GBK', 'utf-8')
      file_write.write(content)
      file_write.flush()
      parse('index.xml',TestHandle())
      file_write.close()
finally:
  	file_read.close()
  	file_write.close()
'''
try:
  while True:
    line = file_read.readline()
    if len(line) == 0: # Zero length indicates EOF
      break
    line_temp.append(line)
  if __name__ == '__main__':
    url = 'http://www.cffex.com.cn/fzjy/ccpm/201303/07/index.xml'
    file_write = open('index.xml', 'w')
    file_write.seek(0,0)
    content = urllib2.urlopen(url).read()
    content = content.decode('gbk').encode('UTF-8')
    content = content.replace('GBK', 'utf-8')
    file_write.write(content)
    file_write.flush()
    lt = []
    parse('index.xml',TestHandle(lt))
    file_write.close()
finally:
    file_read.close()
    file_write.close()
'''