# import the pandas library and aliasing as pd
import pandas as pd

list_data = [10,20,30]
labels = ['a','b','c']
dict_data = {'i':10, 'j':20, 'k':30}

# Creating pandas series
'''
print(pd.Series(data=list_data))
print(pd.Series(data=list_data, index=labels))
print(pd.Series(dict_data))
'''

series1 = pd.Series([1,2,3,4], index=['USA', 'German', 'IND', 'UK'])
print('Series1:\n', series1)
print()
series2 = pd.Series([1,2,3,4], index=['Italy', 'German', 'IND', 'Japan'])
print('Series2:\n', series2)
print()

# print('Sum of two series:\n', series1+series2)

# Access pandas series data by using Index
print('IND: ', series1['IND'])