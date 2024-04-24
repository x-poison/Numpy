import numpy as np

#create an Array
arr = np.array([[[0,1,2,3,4,5], [6,7,8,9,0,10]], [[0,1,2,3,4,5],[6,7,8,9,0,1]]])

#slice the Array
sliced_Array = arr[0:2, 1:4]

"""
the output is:
[[[ 6  7  8  9  0 10]]

 [[ 6  7  8  9  0  1]]]
"""
print(sliced_Array)