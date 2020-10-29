import pandas as pd 	# import the pandas library and aliasing as pd
import numpy as np 		# import the numpy library and aliasing as np

from numpy.random import randn

# creating data frame with row and column
df = pd.DataFrame(randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
# print(df)

# Access data frame by selecting Column
'''
print(df['W'])
print(df[['W', 'Z']])
'''

# Creating new column in existing data frame
'''
df['new_column'] = df['W'] + df['Y']
print(df)


print(df.drop('new_column', axis=1))	# Temporary deleting column from data frame

print(df.drop('A', axis=0))		# Temporary deleting row from data frame
print()
print(df)

print()
df.drop('new_column', axis=1, inplace=True)		# Permanent deleting column from data frame
print(df)
'''

# Access data frame by selecting Row 
'''
print(df.loc['B'])
print(df.iloc[1])
'''

# Selecting subset of row and column
print(df)
print()
print(df.loc['C','Y'])
print(df.loc[['C','E'], ['Y','Z']])


