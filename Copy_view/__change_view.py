import numpy as np

#create an Array
arr = np.array([0,1,2,3,4,5,6,7,8,9])

#view array
arr2 = arr.view()

#edit arr2
arr2[0] = 30

#print noe to see
print(arr)
print(arr2)