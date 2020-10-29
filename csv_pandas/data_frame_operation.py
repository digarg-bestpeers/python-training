import pandas as pd
import numpy as np

from numpy.random import randn
df = pd.DataFrame({'col1':[1,2,3,4], 'col2':[111,222,333,222], 'col3':['abc','def','ghi','xyz']})
print(df)

# print(df.head(2))	# To print first Two records

# print(df['col2'].unique())		# To print only unique value of accessed respective column

# print(df['col2'].nunique())			# To print number of unique value of accessed respective column

# print(df['col2'].value_counts())	# To count per value of respective column

print(df['col2'].sort_values())		# Sorting respective column 
print(df.sort_values(by='col2'))
print(df)