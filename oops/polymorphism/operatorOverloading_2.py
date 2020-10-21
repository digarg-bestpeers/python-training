class Student:
	def __init__(self, name, marks):
		self.name = name
		self.marks = marks

	def __gt__(self,other):					# magic method: override method on > operator
		return self.marks>other.marks

student1_name = input("Enter First Student Name: ")
student1_marks = int(input("Enter First Student Marks: "))
student2_name = input("Enter Second Student Name: ")
student2_marks = int(input("Enter Second Student Marks: "))

student1_object = Student(student1_name, student1_marks)
student2_object = Student(student2_name, student2_marks)

print("\nStudent record with highest marks:")
if(student1_object>student2_object):
	print("Student Name: {}\nMarks: {}".format(student1_object.name, student1_object.marks))
else:
	print("Student Name: {}\nMarks: {}".format(student2_object.name, student2_object.marks))