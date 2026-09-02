import numpy as np

sales = np.array([
    [100, 200, 300, 400],
    [150, 250, 350, 450],
    [120, 220, 320, 420]
])

#print first row
print(sales[0])
print(sales[0,:])

#print last row
print(sales[-1,:])
print(sales[-1,:])

#Print the value 350.
print(sales[1,2])

#Print the second column.
print(sales[:,1])

#Print the last column.
print(sales[:,-1])

#Print the first two rows.
print(sales[0:2,:])

#Print the first three columns.
print(sales[:,0:3])

#Reverse the columns.
print(sales[::-1,::-1])

#Extract the last two rows and last two columns.
print(sales[-2:,-2:])

#Create a NumPy array representing 5 students × 4 subjects:

marks = np.array([
    [90,78,98,99],
    [67,76,54,78],
    [66,44,55,67],
    [60,89,90,78],
    [65,90,78,90]
])

#Get Student 1's mark
print(marks[0,:])

#Get Student 5's marks
print(marks[-1,:])
print(marks[4,:])

#Get all students' 2nd sub marks
print(marks[:,1])

#Get the first 3 students
print(marks[0:3])

#Get the last 2 students
print(marks[-2:,:])

#Get 1st sub + 2nd sub marks for all students
print(marks[:,0]+marks[:,1])

#Get the last 2 subjects for the first 3 students
print(marks[:3,-2:])