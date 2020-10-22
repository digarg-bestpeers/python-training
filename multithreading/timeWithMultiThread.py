# Execution time calculated with multithread
import time
from threading import *
def doubles(numbers):
	for num in numbers:
		time.sleep(1)
		print('Double: ', 2*num)

def square(numbers):
	for num in numbers:
		time.sleep(1)
		print('square: ', num*num)

numbers = [1,2,3,4,5,6]
begintime = time.time()
thread_object1 = Thread(target = doubles, args=(numbers,))
thread_object2 = Thread(target = square, args=(numbers,))
thread_object1.start()
thread_object2.start()
thread_object1.join()
thread_object2.join()
endtime = time.time()
print('Total time taken: ', endtime-begintime)