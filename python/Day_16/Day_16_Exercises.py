import numpy as np

#Exercise 1
prices = np.array([100, 250, 300, 450, 500])

print(f'total price: {np.sum(prices)}')
print(f'average price: {np.mean(prices)}')
print(f'max price: {np.max(prices)}')
print(f'min price: {np.min(prices)}')

#Exercise 2
marks = np.array([78, 85, 92, 67, 88])

print(f'total marks: {np.sum(marks)}')
print(f'average marks: {np.mean(marks)}')
print(f'max marks: {np.max(marks)}')
print(f'min marks: {np.min(marks)}')

#Exercise 3 — 2D Array
sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]
])

print(f'total sales: {np.sum(sales)}')
print(f'average sales: {np.mean(sales)}')
print(f'max sales: {np.max(sales)}')
print(f'min sales: {np.min(sales)}')
print(f'each month sales: {np.sum(sales,axis = 0)}')
print(f'each sales person: {np.sum(sales,axis=1)}')