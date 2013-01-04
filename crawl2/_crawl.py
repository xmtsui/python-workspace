#!/usr/bin/python
# Filename : crawl.py
import string
import urllib2
from sgmllib import SGMLParser
 
file_object = open('code.txt')
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
	#  print item
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
		self.is_td = ""
		self.name = []
	def start_td(self, attrs):
		for k,v in attrs:
	          if k == 'class' and v == 'yfnc_tabledata1':
		    self.is_td = 1
	def end_td(self):
		self.is_td = ""
	def handle_data(self, text):
		if self.is_td == 1:
			self.name.append(text)

#date1 = '10/31/2012'
#date2 = '9/28/2012'
day1 = '01'
month1 = '10'
year1 = '1990'
day2 = '30'
month2 = '11'
year2 = '2012'
for item1 in t:
	page_index = 0
        for page_index in range(0,4):
	  re = 66 * page_index
	  if re == 0 :
	    page_index_tmp = '1'
	  else:
	    page_index_tmp = '%d' % re
	  url = 'http://finance.yahoo.com/q/hp?s=' + item1 + '&a=' + month1 + '&b=' + day1 + '&c=' + year1 + '&d=' + month2 + '&e=' + day2 +'&f=' + year2 + '&g=m&z=66&y=' + page_index_tmp
          content = urllib2.urlopen(url).read()
	  listtd = ListTD()
	  listtd.feed(content)
	  i = 0
	  listtdlen = len(listtd.name)
	  for i in range(0, listtdlen):
	    if(i+6 >= listtdlen):
	      break
	    try:
	      string.atof(listtd.name[i])
	    except ValueError,e:
	      #print "error",e,"on line",i
	      print item1,'	',
	      print listtd.name[i],'	',
	      print listtd.name[i+6]
	    i+=1
	  page_index+=1
