def decorator_function(main_functionAsArgument):	# decorator function
	def inner_function():
		number1 = main_functionAsArgument()
		result = number1 + 5
		return result
	return inner_function

def decorator_function2(functionAsArgument):	# decorator function
	def inner_function():
		number1 = functionAsArgument()
		result = number1 * 5
		return result
	return inner_function


@decorator_function2
@decorator_function		# extended functionality using decorator function
def main_function():	# function creation
	return 10

print(main_function())
