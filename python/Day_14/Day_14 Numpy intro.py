import numpy as np

#numpy : Numerical Python , it is a Python library designed for: calculation , ML, large datasets , mathematical operation.
#One major advantage is that NumPy allows mathematical operations directly on the entire array.

#Creating NumPy Arrays:NumPy is used to work with arrays. The array object in NumPy is called ndarray.
#We can create a NumPy ndarray object by using the array() function.

arr = np.array([10,20,30,40,50]) #with list
print(arr)

arr1 = np.array((1,2,3,4,5,6))
print(arr1)

#Dimensions in Arrays:A dimension in arrays is one level of array depth (nested arrays).

#0-D Arrays:0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

arr2 = np.array([42]) #Create a 0-D array with value 42
print(arr2)

#1-D Arrays:An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

arr3 = np.array([10,20,30]) #Create a 1-D array containing the values 10,20,30
print(arr3)

#2-D Arrays:An array that has 1-D arrays as its elements is called a 2-D array.

arr4 = np.array([[10,20,30],[40,50,60]])
print(arr4)

#3-D arrays:An array that has 2-D arrays (matrices) as its elements is called 3-D array

arr5 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr5)

#Dimensions: ndim , The dimension tells you how many levels of arrays you have.
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)
print(arr5.ndim)

#Higher Dimensional Arrays: When the array is created, you can define the number of dimensions by using the ndmin argument.

arr = np.array([1, 2, 3, 4,5], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

#Shape:.shape tells you how many elements exist along each dimension.

a = np.array([1,2,3,4])
print(a.shape) #There are 4 elements.

b = np.array([[1,2,3,4],[5,6,7,8]])
print(b.shape)  #it gives (2,4) it means 2 rows and 4 column.

c = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(c.shape) #(2,2,3) it has 2 blocks , 2 rows in each block , 3 colum in each row

#Data Types:NumPy arrays have a data type.
#The NumPy array object has a property called dtype that returns the data type of the array:
#we cannot mixup the data types in arrays

d = np.array([1,2,3,4])
print(d.dtype)
e = np.array(['k','m'])
print(e.dtype)
f = np.array([1.2,3.5])
print(f.dtype)
g = np.array([True,False])
print(g.dtype)

#