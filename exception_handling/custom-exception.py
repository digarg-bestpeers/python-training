class TooYoungException(Exception):
	def __init__(self, arg):
		self.msg = arg

class TooOldException(Exception):
	def __init__(self, arg):
		self.msg = arg

age = int(input("Enter Age: "))
if age>60:
	raise TooYoungException("Your age is expired...")
elif age<18:
	raise TooOldException("You are not eligible for marriage....")
else:
	print("You will get match soon!!")