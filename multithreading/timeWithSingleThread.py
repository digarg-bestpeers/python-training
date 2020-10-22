# Execution time calculated without multithread
import time
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
doubles(numbers)
square(numbers)
endtime = time.time()
print('Total time taken: ', endtime-begintime)