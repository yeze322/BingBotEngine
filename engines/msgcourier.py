import search.engine as searchEngine
import dialog.engine as dialogEngine

class MSG_TYPE_ENUM:
	QUERY, DIALOG = range(2)

def __askSeachEngine(question):
	return searchEngine.Ask(question)
def __askTheMagicConch(question):
	return dialogEngine.Ask(question)

HANDLERS = {
	MSG_TYPE_ENUM.QUERY : __askSeachEngine,
	MSG_TYPE_ENUM.DIALOG : __askTheMagicConch
}

def msgTypeSwitcher(question):
	if question == 'hello':
		return MSG_TYPE_ENUM.DIALOG
	else:
		return MSG_TYPE_ENUM.QUERY

def GetResponse(question):
	msgtype = msgTypeSwitcher(question)
	func = HANDLERS[msgtype]
	return func(question)

if __name__ == '__main__':
	print GetResponse("password")
	print '-------------------'
	print GetResponse('hello')
