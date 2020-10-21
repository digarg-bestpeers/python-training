class Rbi:
	def homeLoan(self):
		print('Home Loan and Interest Rate is: 7')

	def educationLoan(self):
		print('Education Loan and Interest Rate is: 10')

class icici(Rbi):
	def educationLoan(self):			# Override parent class method
		print('Education Loan and Interest Rate is: 12')

object = icici()
object.homeLoan()
object.educationLoan()





