class xx:
	def __init__(self):
		self.vvv = 1
	def __enter__(self):
		return self.vvv
	def __exit__(self,ctx_type, ctx_value, ctx_traceback):
		pass

with xx() as x:
	print x