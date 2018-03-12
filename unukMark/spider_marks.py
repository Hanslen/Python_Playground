import urllib
import urllib2
import cookielib
filename = 'cookie.txt'

cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
	'UserName':'xxxx',
	'Password':'xxxxx'
	})
loginUrl = "https://bluecastle.nottingham.ac.uk/Account/Login"
result = opener.open(loginUrl, postdata)
cookie.save(ignore_discard=True, ignore_expires=True)
gradeUrl = "https://bluecastle.nottingham.ac.uk/my-marks"
result = opener.open(gradeUrl)
print result.read()