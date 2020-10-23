# To check Thread identification Number
from threading import *
def childFunction():
	print('child thread')

thread_object = Thread(target=childFunction)
thread_object.start()

print('Main Thread identification Number: ', current_thread().ident)
print('Child Thread identification Number: ', thread_object.ident)