try:
	print("outer try block")
	try:
		print("Inner try block")
		print(10/0)
	except ZeroDivisionError:
		print("Inner except block")
	finally:			# Always accessable wheather exception raised or not
		print("Inner finally block")
except:
	print("outer except block")
finally:
	print("outer finally block")