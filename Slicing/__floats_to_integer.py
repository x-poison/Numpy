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

#lets declare new Array and use int as parameter
arr2 = np.array([1.2,3.2,1.5,3.7,4.5,5.7])
newArr2 = arr2.astype(int)
print(newArr2.dtype)
#output => int32

print(newArr2)
#output => [1 3 1 3 4 5]

##############################################################################################