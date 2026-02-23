import numpy as np
"""
print("\n") is used to leave a blank line in the output
"""
# creating a regular list
myList = [20,30,40]
#----numpy usage----
print(np.array(myList))
# matrix list
matrixList = [[10,20,30],[20,30,40],[30,40,50]]
print(np.array(matrixList))
print("\n")
# range-arange
print(np.arange(0,10))
print(np.arange(0,10,2))
# zeros (can be used in image processing)
print(np.zeros(5))
print(np.zeros((3,3)))
# ones
print("\n")
print(np.ones(5))
print(np.ones((3,3)))
# linspace evenLinspace
print("\n") 
print(np.linspace(0,20,10)) # finds 10 equally spaced numbers between 0-20 (inclusive)
# eye creates an identity matrix based on the given value
print("\n")
print(np.eye(3)) # identity matrix: a matrix that has no effect when multiplied with another matrix
# random
print("\n")
print(np.random.randn(4)) # returns an array
print(np.random.randn(3,3)) # returns a matrix
print(np.random.randint(1,10)) # a random value between 1 and 10
print(np.random.randint(1,100,5)) # an array of 5 elements between 1 and 100
array1 = np.random.randint(1,100,10)
print(array1)
# numpy array methods
print("\n")
array2 = np.arange(0,30)
print(array2)
print(array2.reshape(5,6)) # converted to a matrix
print("\n")
print(array1.max()) # finds the maximum element in the array
print(array1.min()) # finds the minimum element in the array
print(array1.argmax()) # finds the index of the maximum value in the array
print(array1.argmin()) # finds the index of the minimum value in the array
print(array1.shape) # gives the number of elements in the array
# numpy operations
print("\n")
print(array1[1])
print(array2[3:5])
array1[2:5] = -7 # replaces the values between the given indices with the specified value
print(array1)
array1[:] = 50
print(array1)
slicedArray = array1[3:7] # we've done this before
print(slicedArray)
slicedArray[:] = 20 # when this change is made, array1 is also affected
print(slicedArray)
print("\n")
print(array1) # to prevent this, the array should be copied first and operations should be done on the copy
array1copy = array1.copy() # after doing it this way, if the above operations are performed, the original array1 won't change
# Matrix
print("\n")
list1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix1 = np.array(list1)
print(matrix1)
print("\n")
print(matrix1[1])
print(matrix1[1][1])
print(matrix1[1,1])
print(matrix1[2:,])
print(matrix1[:,1]) # the middle column
print(matrix1[:,1:2]) # the middle column from top to bottom
print(matrix1[2:,2:]) # 3rd column 3rd row
list2 = [[1,2,3,10],[4,5,6,11],[7,8,9,12],[13,14,13,15]]
matrix2 = np.array(list2)
print("\n")
print(matrix2)
print("\n")
print(matrix2[[0,3,2]]) # this allowed us to get the 1st, 3rd, and 2nd rows
# numpy array operations
print("\n")
array3 = np.random.randint(1,100,20)
print(array3)
resultArray = array3 > 20
print("\n")
print(resultArray)
print("\n")
print(array3[resultArray])
print("\n")
print(array3[array3>20])
print("\n")
print("operations")
print(array3+array3)
print(array3*array3)
print(array3/array3) 
print(array3-array3) 
print(np.sqrt(array2)) # take the square root
