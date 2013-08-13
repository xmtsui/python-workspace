#!/usr/bin/python
# Filename : crawl.py
import urllib2
from sgmllib import SGMLParser
 
file_object = open('name1.txt')
line_temp = []
t = []
try:
	while True:
		line = file_object.readline()
		if len(line) == 0: # Zero length indicates EOF
			break
		line_temp.append(line)
	for item in line_temp:
		t = item.split('	')
	#for item in t:
	#print item
finally:
     file_object.close( )

class ListTR(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_tr = ""
		self.name = []
	def start_tr(self, attrs):
		self.is_tr= 1
	def end_tr(self):
		self.is_tr = ""
	def handle_data(self, text):
		if self.is_tr == 1:
			self.name.append(text)

class ListTD(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_table = ""
		self.name = []
	def start_table(self, attrs):
		self.is_table= 1
	def end_table(self):
		self.is_table = ""
	def handle_data(self, text):
		if self.is_table == 1:
			self.name.append(text)

date1 = '10/31/2012'
date2 = '9/28/2012'

for item1 in t:
	url = 'http://www.nasdaq.com/symbol/' + item1 + '/short-interest'
	content = urllib2.urlopen(url).read()
	listtd = ListTD()
	listtd.feed(content)
	i = 0
	for item in listtd.name:
		if item.startswith(date1):
			print item1,
			print item.decode('gbk').encode('utf8'),
			print listtd.name[i+1].decode('gbk').encode('utf8'),
			print listtd.name[i+2].decode('gbk').encode('utf8'),
			print listtd.name[i+3].decode('gbk').encode('utf8')
		elif item.startswith(date2):
			print item1,
			print item.decode('gbk').encode('utf8'),
			print listtd.name[i+1].decode('gbk').encode('utf8'),
			print listtd.name[i+2].decode('gbk').encode('utf8'),
			print listtd.name[i+3].decode('gbk').encode('utf8')
		i+=1
#print '----------' 
#for item in listtd.name:
#	print item.decode('gbk').encode('utf8')
