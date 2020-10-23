# Division of Two numbers execution with try and except block
try:
	first_number = int(input("Enter First Number: "))
	second_number = int(input("Enter Second Number: "))
	result = first_number / second_number
	print('Division of {} and {} is: {}'.format(first_number,second_number,result))
except ZeroDivisionError:
	print("please provide non zero number in denominator")