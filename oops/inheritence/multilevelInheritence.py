class Person:
	"Base class person information"
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def displayPerson(self):
		return 'Person Information:-\nName: {}\nAge: {}'.format(self.name, self.age)

class Student(Person):
	'Student information derived from person class'
	def __init__(self, name, age, rollno, marks):
		super().__init__(name, age)
		self.rollno = rollno
		self.marks = marks

	def displayStudent(self):
		return 'Student Information:-\nName: {}\nAge: {}\nRoll Number: {}\nMarks: {}'.format(self.name, self.age, self.rollno, self.marks)

class Employee(Student):
	'Employee information derived from student class'
	def __init__(self, name, age, rollno, marks, id, technology):
		super().__init__(name, age, rollno, marks)
		self.id = id
		self.technology = technology

	def displayEmployee(self):
		return 'Employee Information:-\nName: {}\nAge: {}\nRoll Number: {}\nMarks: {}\nEmployee Id: {}\nTechnology: {}'.format(self.name, self.age, self.rollno, self.marks, self.id, self.technology)

e1 = Employee('Zara',24,102,85,1001,'python')
print(e1.displayPerson())		# Base class method accessed
print()
print(e1.displayStudent())		# parent class method accessed
print()
print(e1.displayEmployee())
print()