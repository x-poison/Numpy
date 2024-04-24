import numpy as np

#create 3d Array
arr = np.array([[[1,2,3,4,5], [6,7,8,9,0]], [[1,2,3,4,5], [6,7,8,9,0]]])

#print 3rd element of the 2nd Array of the first array => 8
print(f'The answer is:  {arr[0, 1, 2]}')