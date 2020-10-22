# Creating thread without using class
from threading import *
def display():
	for i in range(10):
		print("Child Thread")

object = Thread(target=display)
object.start()
for i  in range(10):
	print("Main Thread")