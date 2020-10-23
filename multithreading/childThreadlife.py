# To check child thread ia live or dead
from threading import *
import time
def childFunction():
	print(current_thread().name, '...started')
	time.sleep(3)
	print(current_thread().name, '...ended')

object_thread1 = Thread(target=childFunction, name='ChildThread-1')
object_thread2 = Thread(target=childFunction, name='ChildThread-2')
object_thread1.start()
object_thread2.start()
print(object_thread1.name, 'is Alive: ', object_thread1.isAlive())
print(object_thread2.name, 'is Alive: ', object_thread2.isAlive())
time.sleep(10)
print(object_thread1.name, 'is Alive: ', object_thread1.isAlive())
print(object_thread2.name, 'is Alive: ', object_thread2.isAlive())