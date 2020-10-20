class Student:
	'Student class information'
	def __init__(self, name, course):
		self.name = name
		self.course = course

	def studentDisplay(self):
		return 'Student Name: {}\ncourse: {}'.format(self.name, self.course)

class Employee:
	'Employee class information'
	def __init__(self, id, technology):
		self.id = id
		self.technology = technology

	def employeeDisplay(self):
		return 'Employee id: {}\ntechnology: {}'.format(self.id, self.technology)

def person(object):					# function impliment polymorphism concept
	if hasattr(object, 'studentDisplay'):
		print(object.studentDisplay())
		print()
	elif hasattr(object, 'employeeDisplay'):
		print(object.employeeDisplay())
		print()


studentObject = Student('Dinesh','BTech')
employeeObject = Employee(101, 'python')

person(studentObject)			# function called
person(employeeObject)