# Display multi child threads name with extending Thread class
from threading import *
class MyThread(Thread):
	def run(self):
		for i in range(10):
			print('Child Thread Executed by: ', current_thread().getName())

object1 = MyThread()
object2 = MyThread()
object3 = MyThread()
object1.start()
object2.start()
object3.start()

