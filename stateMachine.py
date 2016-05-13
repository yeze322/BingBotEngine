import urlParser

def askTheMagicConch(text):
	response = urlParser.Search(text)
	if response:
		answer = "`Are you asking:` \n\t\t" + "*{0}*".format(response[0]) + '?\n'
		answer += "`I know that...` \n\t" + response[1] + '\n'
		answer += '`Please click this URL:` \n\t' + response[2] + '\n'
	else:
		answer = "Sorry, cannot answer this question."
	return answer