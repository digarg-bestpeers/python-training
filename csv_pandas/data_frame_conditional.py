# Conditional Selection from data df[fram]e

import pandas as pd 	# import the pandas library and aliasing as pd
import numpy as np 		# import the numpy library and aliasing as np

from numpy.random import randn

# creating data frame with row and column
df = pd.DataFrame(randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
# print(df)

# print(df>0)

# print(df[df>0])

# print(df['W']>0)

# print(df[df['W']>0][['Y','X']])

# Reset Index with default value
print(df.reset_index())

df['states'] = 'UT MP UP MH RJ'.split()
print(df)
# print(df.set_index('states'))		# Temporary set index value

df.set_index('states', inplace=True)		# Permanent set index value
print(df)



