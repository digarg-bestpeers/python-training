# Creating thread without extending Thread class
from threading import *
class Test:
	def display(self):
		for i in range(10):
			print('Child Thread-2')

object = Test()
thread_object = Thread(target=object.display)
thread_object.start()
for i in range(10):
	print('Main Thread-2')