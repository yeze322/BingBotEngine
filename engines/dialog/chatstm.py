from state_machine import *

@acts_as_state_machine
class GreetingBot:
	Idle = State(initial=True)
	AfterHello = State()
	AfterEmail = State()
	Done = State()

	getName = Event(from_states=A, to_state=B)
	getEmail = Event(from_states=B, to_state=C)

	errInfo = Event(from_states=(A,B), to_state=A)

	@before('getName')
	def printName(self):
		print "please input Name"
	@before('getEmail')
	def printEmail(self):
		print "please input email"
	@before('errInfo')
	def printErr(self):
		print "wrong input, will return to init state"


stm = STM()
stm.errInfo()