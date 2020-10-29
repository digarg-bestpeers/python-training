# Delete record from Id and generate new CSV file

import pandas as pd 	# import the pandas library and aliasing as pd

fileName = input('Enter csv file name: ')
info_data = pd.read_csv(fileName)		# Read csv file and create it as data frame
info_data.set_index('Id', inplace=True)		# Setting column Id as new index

user_id = input("Enter Id which you want to delete: ")

try:
	for Id in user_id:
		if Id is not ',':
			info_data.drop(int(Id), axis=0, inplace=True)	# Delete row which user provided
	newFileName = input('Enter file name to create with updated data: ')
	info_data.to_csv(newFileName+'.csv', sep=',', index=True, header=True)	# Create new csv file
	print('File created successfully...Done')
except:
	print('Entered wrong id')

