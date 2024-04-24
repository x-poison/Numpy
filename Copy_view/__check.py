import numpy as np

#create an Array
arr = np.array([0,1,2,3,4,5,6])

y = arr.copy()
x = arr.view()

print(y.base)
print(x.base)