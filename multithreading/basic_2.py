# Displaying Two thread names
from threading import *
def display():
	print('This code (display function) executed by Thread: ', current_thread().getName())

t = Thread(target=display)		# MainThread creates child thread object
t.start()						# MainThread starts ChildThread
print('This code executed by Thread: ', current_thread().getName())
