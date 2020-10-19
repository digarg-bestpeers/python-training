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

	def __str__(self):			# overwrite str method
		return self.name

	def displayStudent(self):
		return 'Student Information:-\nName: {}\nAge: {}\nRoll Number: {}\nMarks: {}'.format(self.name, self.age, self.rollno, self.marks)

s1 = Student('Dinesh', 26, 101, 80)
print(s1)
print()
print(s1.displayPerson())   # parent class method accessed
print()
print(s1.displayStudent())   # child class method accessed
