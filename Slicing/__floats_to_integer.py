import numpy as np

#create an Array
arr = np.array([1.2,3.2,1.5,3.7])

#create new Array to convert arr
newArr = arr.astype('i')

#print newArr
print(newArr)
#output => [1 3 1 3]

#print data type of newArr
print(newArr.dtype)
#output => int32