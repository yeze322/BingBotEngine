fp = open('token','rb')
token = fp.readline()
fp.close()

import time
from slackclient import SlackClient
from engines import msgcourier

sc = SlackClient(token)
if sc.rtm_connect():
	while True:
		time.sleep(0.6)
		query = sc.rtm_read()
		if query == []:
			continue
		else:
			#continue
			q = query[0]
			print q
			if 'reply_to' in q:
				continue
			if 'type' in q and q['type'] == 'message':
				text = q['text']
				channel = q['channel']
				answer = msgcourier.GetResponse(text);
				sc.rtm_send_message(channel, answer)
else:
	print "Connection Failed, invalid token?"
