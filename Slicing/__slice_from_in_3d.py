import numpy as np

#create an Array 3D
arr = np.array([[[0,1,2,3,4,5], [6,7,8,9,0,10]], [[0,1,2,3,4,5],[6,7,8,9,0,1]]])

#access the second array of the second array
#slice the array
sliced_Array = arr[1,1, 0:4]

#print the sliced Array
print(sliced_Array)