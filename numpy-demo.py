import numpy as np
#create 1D array
a = np.array([1,2,3,4,5,6,7])

print(a)

#print the dimention
print(a.ndim)
#print the shape of the array
print(a.shape)

#create 1D array
b = np.array([[1.2,4.5,7.0,6.2,2.2,9.1],[3.1,66.4,7.9,4.3,6.8,22.1]])

print(b)
#print the shape of the array
print(b.shape)
#print the dimention
print(b.ndim)
#print the data type of the array
print(b.dtype)

#get a specific element [raw,column]
b[1,3]

b[0,:]

#get all 0s metrix

np.zeros(4)