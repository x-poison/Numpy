"""
This module demonstrates basic operations with NumPy arrays,
which are efficient data structures for numerical computations in Python.
NumPy provides support for multi-dimensional arrays and various mathematical
operations, making it suitable for tasks like data manipulation, linear
algebra, and statistical analysis.
"""

import numpy as np

#deffine an Array here
arr = np.array([0,1,2,3,4,5,6,7,8,9])

#print Data Type of the arr
data_type = arr.dtype

print(data_type)
#Output => int32