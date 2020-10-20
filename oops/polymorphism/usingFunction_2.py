class Student:
	'Student class information'
	def __init__(self, name, location):
		self.name = name
		self.location = location

	def infoDisplay(self):
		return 'Student Name: {}\nLocation: {}'.format(self.name, self.location)

class Employee:
	'Employee class information'
	def __init__(self, name, location):
		self.name = name
		self.location = location

	def infoDisplay(self):
		return 'Employee Name: {}\nLocation: {}'.format(self.name, self.location)

def person(object):				# function impliment polymorphism concept
	print(object.infoDisplay())
	print()

studentObject = Student('Sam','Bhopal')
employeeObject = Employee('Dinesh', 'Indore')

person(studentObject)			# function called
person(employeeObject)



