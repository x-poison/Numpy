import numpy as np

#create an Array
arr = np.array([0,1,2,3,4,5,6,7,8,9])

#create and view the arr
arr2 = arr.view()

#Edit 1st arr
arr[1] = 10

#print arrays
print(arr)
print(arr2)
