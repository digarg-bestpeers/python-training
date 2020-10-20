class Student:
	'Student class information'
	def __init__(self, name, location):
		self.name = name
		self.location = location

	def infoDisplay(self):
		return 'Student Name: {}\nLocation: {}'.format(self.name, self.location)

class Employee:
	'Employee class information'
	def __init__(self, id, location):
		self.id = id
		self.location = location

	def infoDisplay(self):
		return 'Employee Id: {}\nLocation: {}'.format(self.id, self.location)

student_object = Student('Dinesh','Indore')
employee_object = Employee(101, 'Delhi')

for object in (student_object, employee_object):
	print(object.infoDisplay())
	print()