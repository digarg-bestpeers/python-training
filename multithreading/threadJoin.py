# Use of Join method with Thread object
from threading import *
import time
def display():
	for i in range(10):
		print('Child Thread')
		time.sleep(2)

thread_object = Thread(target=display)
thread_object.start()
# thread_object.join()		# Main Threed has to wait completion of Child Thread execution
thread_object.join(10)		# Main Thread wait child thread execution till 10 seconds after completion of this time Main thread will also active
for i in range(10):
	print('Main Thread')
	time.sleep(2)