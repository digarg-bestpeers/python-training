# To find active Thread count
from threading import *
import time
def childFunction():
	print(current_thread().name, '...started')
	time.sleep(3)
	print(current_thread().name, '...ended')

print('The number of active Threads: ', active_count())
object_thread1 = Thread(target=childFunction, name='ChildThread-1')
object_thread2 = Thread(target=childFunction, name='ChildThread-2')
object_thread3 = Thread(target=childFunction, name='ChildThread-3')
object_thread1.start()
object_thread2.start()
object_thread3.start()
print('The number of active Threads: ', active_count())
time.sleep(10)
print('The number of active Threads: ', active_count())
