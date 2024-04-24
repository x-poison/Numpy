import numpy as np

#create an Array
arr = np.array([1,2,3,4,5,6,7,0])

#create new Array and convert arr to boolean
newArr = arr.astype(bool)

#print data types
print(arr.dtype) #output int32
print(newArr.dtype) #output => bool

#print converted array
print(newArr)
#output => [ True  True  True  True  True  True  True False]