#!/usr/bin/python
# coding=utf-8
# Filename : crawl_0628.py
import urllib2
import string
from xml.sax.handler import ContentHandler  
from xml.sax import parse

#url = 'http://www.cffex.com.cn/fzjy/mrhq/index_5351.xml'
class TestHandle(ContentHandler):
    date = ""
    result = 0.0
    def __init__(self):
        self.i = 0
        self.flag1 = 0
        self.flag2 = 0
        self.date = ""
    def startElement(self,name,attrs):
        # print 'name:',name, 'attrs:',attrs.keys()
        self.i
        if name == "a":
          self.flag1 = 1
        else:
          self.flag1 = 0
        
        if name == "h":
          self.flag2 = 1
        else:
          self.flag2 = 0

    def endElement(self,name):
        # print 'endname',name
        self.i
    def characters(self,chars):
      if self.flag1 == 1:
        if TestHandle.date != chars:
          print TestHandle.date, TestHandle.result
          TestHandle.date = chars
          TestHandle.result = 0.0
          self.date = chars
        else:
          self.date = chars
      if self.flag2 == 1:
        if TestHandle.date == self.date:
          TestHandle.result += string.atof(chars)

parse('index_5351.xml',TestHandle())