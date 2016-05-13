fp = open('token','rb')
token = fp.readline()
fp.close()

import time
from slackclient import SlackClient
import urlParser
from stateMachine import askTheMagicConch

sc = SlackClient(token)
if sc.rtm_connect():
	while True:
		time.sleep(0.6)
		query = sc.rtm_read()
		if query == []:
			continue
		else:
			#continue
			qqq = query[0]
			print qqq
			if 'reply_to' in qqq:
				continue
			if 'type' in qqq and qqq['type'] == 'message':
					text = qqq['text']
					channel = qqq['channel']
					answer = askTheMagicConch(text);
					sc.rtm_send_message(channel, answer)
else:
	print "Connection Failed, invalid token?"