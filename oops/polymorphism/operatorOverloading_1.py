class Book:
	def __init__(self, pages):
		self.pages = pages

	def __add__(self, other):		# magic method: override method on + operator
		return self.pages+other.pages

book1_object = Book(100)
book2_object = Book(200)
print("Total Number of Pages: ", book1_object+book2_object)


