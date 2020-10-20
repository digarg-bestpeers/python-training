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

class Employee(Person):
	'Employee information derived from person class'
	def __init__(self, name, age, id, technology):
		super().__init__(name, age)
		self.id = id
		self.technology = technology

	def displayEmployee(self):
		return 'Employee Information:-\nName: {}\nAge: {}\nEmployee Id: {}\nTechnology: {}'.format(self.name, self.age, self.id, self.technology)

s1 = Student('Student One', 22, 105, 75)
print(s1.displayPerson())
print()
print(s1.displayStudent())
print('\n \n')
e1 = Employee('Employee One', 24, 1004, 'Django')
print(e1.displayPerson())
print()
print(e1.displayEmployee())