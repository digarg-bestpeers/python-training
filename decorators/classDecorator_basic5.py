class Check_div:
	def __init__(self, func):
		self.func = func
	def __call__(self, *args, **kwargs):
		if args[1] == 0:
			return "You can't divide with zero denominator!!"
		else:
			return self.func(*args, **kwargs)

@Check_div
def div(a,b):
	return a/b

print(div(10,20))

