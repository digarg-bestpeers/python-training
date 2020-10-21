class Person:
	name = 'Jack'				# public variable declaration
	_mobile = 9999999999		# protected variable declaration
	__account = 11111			# private variable declaration
	
	def info(self):
		print('Access detail from inside the class')
		print('Name: ', self.name)
		print('Mobile: ', self._mobile)
		print('Account: ', self.__account)
		print()

object = Person()
object.info()

print('Access detail from outside the class')
print('Name: ', object.name)				# Accessable public variable
print('Mobile: ', object._mobile)			# Accessable protected variable
print('Account: ', object.__account)		# Not accessable private variable directly

# Access private variable from outside the class indirectly
# print('Account: ', object._Person__account)