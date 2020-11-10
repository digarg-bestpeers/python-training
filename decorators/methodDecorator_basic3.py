def check_name(method):
	def inner(name_ref):
		if name_ref.name == 'Dinesh':
			print("Hey {}.. my another name is also same!!".format(name_ref.name))
		else:
			method(name_ref)
	return inner


class Printing:
	def __init__(self, name):
		self.name = name

	@check_name
	def print_name(self):
		print('Entered name is: ', self.name)


print_obj1 = Printing("Dinesh")
print_obj2 = Printing("Garg")

print_obj1.print_name()
print_obj2.print_name()