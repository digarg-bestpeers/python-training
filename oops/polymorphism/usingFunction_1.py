class Student:
	'Student class information'
	def name(self):
		print('name method of student class')

class Employee:
	'Employee class information'
	def name(self):
		print('name method of employee class')

def person(object):				# function impliment polymorphism concept
	object.name()

studentObject = Student()
employeeObject = Employee()
person(studentObject)			# function called
person(employeeObject)


# Another way to called function
'''
object_list = [Student(), Employee()]
for object in object_list:
	person(object)
'''
