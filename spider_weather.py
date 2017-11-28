__author__='HanslenChen'
import urllib
import urllib2
import re
import thread
import time
import sys
# -*- coding: utf-8 -*-

class Weather:
	def __init__(self):
		self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
		self.headers = {'User-Agent': self.user_agent}
	def getPage(self):
		try:
			url = "http://www.bbc.co.uk/weather/2641170"
			request = urllib2.Request(url, headers=self.headers)
			response = urllib2.urlopen(request)
			# print response.read()
			pageCode = response.read().decode('utf-8')
			pattern = re.compile('<div class=.*?tabbed-forecast.*?<div class=.*?daily__day-header.*?<span class="day-name" aria-label="(.*?)">.*?<span title="Light (.*?)" class="weather-type-image .*?>.*?<span data-unit=.*?>(.*?)<span', re.S)
			items = re.findall(pattern, pageCode)
			for item in items:
				print item[0],item[1],item[2]
			print (time.strftime("%d/%m/%Y   %H:%M:%S"))

		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print "Connection failed..."
	def start(self):
		self.getPage()
spider = Weather()
spider.start()