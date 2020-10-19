
class Employee:
	'Base class for employees'
	empCount = 0

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		print('Total Employee Count: ', Employee.empCount)

	def displayEmployee(self):
		print('Employee Name: ', self.name)
		print('Employee Salary: ', self.salary)

# class attributes
print('Class __name__: ', Employee.__name__)
print('Employee __doc__: ', Employee.__doc__)

# object created of class
emp1 = Employee('Zara',1000)
emp2 = Employee('Sam', 2000)

# instance method called
emp1.displayCount()
emp1.displayEmployee()
emp2.displayCount()

# instance variable called
print("Employe Name: ", emp1.name)
print("Employee Salary: ", emp1.salary)


# class attribute method
print(hasattr(emp1, 'name'))
print(getattr(emp1, 'name'))
setattr(emp1, 'age', 25)
print(getattr(emp1, 'age'))