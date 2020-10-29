# Delete a field value and generate new CSV file 

import pandas as pd 	# import the pandas library and aliasing as pd

fileName = input('Enter csv file name: ')
info_data = pd.read_csv(fileName)		# Read csv file and create it as data frame
info_data.set_index('Id', inplace=True)		# Setting column Id as new index

# length = len(info_data)

print('Welcome here to delete particular field data...')
id_number = int(input('Enter your Id number: '))
field_name = input('Enter Field Name: ').title()

# if(id_number<=length):
# 	try:
# 		data = info_data.loc[id_number][field_name]
# 		info_data.replace(data, '', inplace=True)
# 		newFileName = input('Enter file name to create with updated data: ')
# 		info_data.to_csv(newFileName+'.csv', sep=',', index=True, header=True)
# 		print('Updated csv created successfully...')
# 	except:
# 		print('Please provide proper Field Name')
# else:
# 	print('Please check your Id')

try:
	data = info_data.loc[id_number][field_name]			# Selecting particular field
	info_data.replace(data, '', inplace=True)
	newFileName = input('Enter file name to create with updated data: ')
	info_data.to_csv(newFileName+'.csv', sep=',', index=True, header=True)
	print('File created successfully...Done')
except:
	print('Wrong Id or Field Name')
