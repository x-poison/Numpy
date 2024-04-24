import numpy as np

#Create an Array Here
arr = np.array([0,1,2,3,4,5,6,7,8,9,10,12,14])

#return every other
return_every = arr[::2]

#print the sliced Array will return the beggining and then add 2 to it, then next
print(return_every)

#The output will be [2,4,6,8,12,14]