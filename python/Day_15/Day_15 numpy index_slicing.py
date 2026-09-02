import numpy as np
#NumPy Array Indexing:
'''Array indexing is the same as accessing an array element.
You can access an array element by referring to its index number.
The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.'''

a = np.array([1,2,3,4])
print(a[0]) #1st element
print(a[1]) #2nd element
print(a[2]+a[3]) #it sum up 3rd and 4th element

#Access 2-D Arrays:
'''To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.'''
'''Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.'''

b = np.array([ #1st row index is 0,1,2 , column 0,1,2
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

#syntax : print(variable[row_number,colum_number])
print(b[1,2]) #it gives 1st row 2nd column element
print(b[2,2]) #it gives 2nd row 3rd colum element

#Access 3-D Arrays:
'''To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.'''

c = np.array([ #block index 0,1 / row index 0,1 / column 0,1,2
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
])
#syntax: print(variable[block_number,row_number,column_number])
print(c)
print(c[0,1,2]) #Access the third element of the second array of the first array:
print(c[1,1,1])

#Negative Indexing:Use negative indexing to access an array from the end.

print(a[-1]) #last element
print(b[-1,-1]) #last row and last column
print(b[0,-1]) #row index one and last column
print(c[-1,-1,-1]) #last block , last row , last column
print(c[0,-1,2]) #block index 0, last row , 2nd column


#Slicing arrays:
'''We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].'''

print(a[0:3]) #index 0 to 3 slicing
print(a[:-2]) #index from 0 to -2
print(a[0:3:2]) #step slicing

#Slicing 2-D Arrays
print(b[1,0:2]) #it gives 1st row , 0 to 2 index element
print(b[0:3,0:2]) # all rows , 0 to 2 index element
print(b[:,1]) #all rows fist column
print(b[:,0:2]) #all rows amd first 2 column
print(b[1:3,0:2])