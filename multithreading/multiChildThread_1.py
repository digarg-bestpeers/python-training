# Display multi child threads name without extending Thread class
from threading import *
class Test:
	def display(self):
		for i in range(10):
			print('Child Thread Executed by: ', current_thread().getName())

object = Test()
thread_object1 = Thread(target=object.display)
thread_object2 = Thread(target=object.display)
thread_object3 = Thread(target=object.display)
thread_object4 = Thread(target=object.display)
thread_object1.start()
thread_object2.start()
thread_object3.start()
thread_object4.start()
