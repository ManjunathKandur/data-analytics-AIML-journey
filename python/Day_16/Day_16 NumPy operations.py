import numpy as np

#NumPy Operations:NumPy allows you to perform mathematical operations directly on arrays.

a = np.array([10,20,30,40,50,67])
b = np.array([10,2,3,6,55,78])

#addition
print(a+b)

#subtraction
print(a-b)

#Multiplication
print(a*b)

#Division
print(a/b)

#Power
print(a**2)
print(b**3)

#to do mathematical operation btw 2 arrays , both arrays should be same shape

#Scalar operations:You can also perform an operation between an array and a single number.

c = np.array([78,65,90,56])
print(c+5)
print(c-5)
print(c*5)
print(c/5)

#Aggregations:
sales = np.array([100, 200, 300, 400])
print(sales.sum())
print(sales.mean())
print(sales.max())
print(sales.min())


#Very Important: axis
'''axis=0 → down the rows → column-wise result
axis=1 → across the columns → row-wise result'''

sales = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

print(np.sum(sales, axis = 1))
print(np.max(sales, axis = 1))
print(np.min(sales, axis = 0))