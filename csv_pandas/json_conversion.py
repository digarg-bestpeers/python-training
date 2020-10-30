# Convertind csv data into json form manually

import pandas as pd 	# import the pandas library and aliasing as pd

fileName = input('Enter csv file name: ')
info_data = pd.read_csv(fileName)		# Read csv file and create it as data frame

inner_dict = {}
outer_dict = {}

column_list = info_data.columns 		# To find column name of data frame

for column in column_list:
	for index in range(len(info_data)):
		inner_dict[str(index)] = info_data[column][index]
	outer_dict.update({column:inner_dict})
	inner_dict={}
print('CSV data in json form:\n')
print(outer_dict)

