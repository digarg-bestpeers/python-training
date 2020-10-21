# Method overloading with default argument
class Add:
	def sum(self, number1=None, number2=None, number3=None):
		if(number1!=None and number2!=None and number3!=None):
			print('Sum: ', number1+number2+number3)
		elif(number1!=None and number2!=None):
			print('Sum: ', number1+number2)
		elif(number1!=None):
			print('Sum: ', number1)
		else:
			print('Please provide at least 1 number and maximum 3 number')

object = Add()
object.sum()			# Instance Method called without argument
object.sum(10)			# Instance Method called with one argument
object.sum(10,20)		# Instance Method called with two argument
object.sum(10,20,30)	# Instance Method called with three argument