try:
	first_number = int(input("Enter First Number: "))
	second_number = int(input("Enter Second Number: "))
	print("Division of {} and {} is: {}".format(first_number, second_number, first_number/second_number))
except ZeroDivisionError:
	print("Denominator value can not be Zero")
except:
	print("please provide valid input")