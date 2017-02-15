__author__='HanslenChen'
import urllib
import urllib2
import re
import thread
import time
import sys

class QSBK:
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
		self.headers = {'User-Agent': self.user_agent}
		self.stories= []
		self.enable = False
	def getPage(self, pageIndex):
		try:
			url = "http://www.qiushibaike.com/8hr/page/"+str(pageIndex)+"/"
			request = urllib2.Request(url, headers=self.headers)
			response = urllib2.urlopen(request)
			pageCode = response.read().decode('utf-8')
			return pageCode
		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print "Connection failed..."
				return None
	def getPageItems(self, pageIndex):
		pageCode = self.getPage(pageIndex)
		if not pageCode:
			print 'Loading failed...'
			return None
		pattern = re.compile('<div class="article block untagged mb15" id=.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?</a>(.*?)<div class="stats">.*?<div class="single-clear"></div>',re.S)
		items = re.findall(pattern, pageCode)
		pageStories = []
		for item in items:
			haveImg = re.search('img',item[2])
			if not haveImg:
				replaceBR = re.compile('<br/>')
				text = re.sub(replaceBR, "\n", item[1])
				pageStories.append([item[0].strip(), text.strip()])
		return pageStories
	def loadPage(self):
		if self.pageIndex != 1:
			print "Start Loading... Please wait..."
		if self.enable == True:
			if len(self.stories) < 2:
				pageStories = self.getPageItems(self.pageIndex)
				if pageStories:
					self.stories.append(pageStories)
					self.pageIndex += 1
		if self.pageIndex == 2:
			print "Finish loading, Enter return to continue and Q(Capital) for quiting..."
	def getOneStory(self,pageStories,page):
		for story in pageStories:
			input = raw_input()
			self.loadPage()
			if input == 'Q':
				self.enable = False
				return
			print "Page:%d\nAuthor: %s\nContent:%s" %(page, story[0],story[1])
	def start(self):
		print "Loading some strange stories... Please wait..."
		self.enable = True
		self.loadPage()
		nowPage = 0
		while self.enable:
			if len(self.stories) > 0:
				pageStories = self.stories[0]
				nowPage += 1
				del self.stories[0]
				self.getOneStory(pageStories, nowPage)
spider = QSBK()
spider.start()
