# Renaming of Main Thread and Child Thread
from threading import *
print('Main Thread Name: ', current_thread().getName())	# To print Thread name
current_thread().setName('Dinesh Garg')				# To change Thread name
print('Main Thread Name: ', current_thread().getName())

def display():
	print('Child Thread name: ', current_thread().name)	# To print child Thread name

thread_object = Thread(target=display)
thread_object.setName('MyChild Thread')
thread_object.start()
print('Main Thread Name: ', current_thread().name)		# Another way to print Thread name