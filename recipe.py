__author__='HanslenChen'
import urllib
import urllib2
import re
import thread
import time
import sys
# -*- coding: utf-8 -*-

class Recipe:
    def __init__(self):
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        self.headers = {'User-Agent': self.user_agent}
    
    def getUrls(self, pageId):
        try:
            url = "http://allrecipes.com/recipes/76/appetizers-and-snacks/?page="+str(pageId)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            # print response.read()
            pattern = re.compile('<h3 class="fixed-recipe-card__h3">.*?<a href="(.*?)" data-internal-referrer-link="hub recipe" class="fixed-recipe-card__title-link">', re.S)
            items = re.findall(pattern, pageCode)
            return items
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print "Connection failed..."

    def getPage(self, fetchUrls):
        for singleUrl in fetchUrls: 
            try:
                url = singleUrl
                request = urllib2.Request(url, headers=self.headers)
                response = urllib2.urlopen(request)
                pageCode = response.read().decode('utf-8')
                pattern = re.compile('itemprop="ingredients">(.*?)</span',re.S)
                items = re.findall(pattern, pageCode)
                print url
                print items
                # print (time.strftime("%d/%m/%Y   %H:%M:%S"))

            except urllib2.URLError, e:
                if hasattr(e, "reason"):
                    print "Connection failed..."

recipe = Recipe()
fetchUrls = []
for i in range(1, 2):
    fetchUrls.extend(recipe.getUrls(i))
    print "Finish fetching pageId: "+str(i)
print "Start getting recipe"
recipe.getPage(fetchUrls)