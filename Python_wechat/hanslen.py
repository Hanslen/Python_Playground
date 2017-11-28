import re
import time
import itchat
from itchat.content import *
@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
def text_reply(msg):
	if msg['Type'] == 'Text':
		reply_content = msg['Text']
	friend = itchat.search_friends(userName=msg['FromUserName'])
	if(itchat.search_friends(userName=msg['FromUserName'])==itchat.search_friends(wechatAccount='wzh14864')[0]):
		#itchat.send("Hello",toUserName=msg['FromUserName'])
		print "WOW"
itchat.auto_login()
itchat.run()
# while True:
# 	print "Running"
# 	itchat.send("Hello, Father", toUserName='ysyyyjm')
