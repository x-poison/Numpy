import numpy as np

#create an Array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

#reshape
newarr = arr.reshape(2, 2, -1)

print(newarr)