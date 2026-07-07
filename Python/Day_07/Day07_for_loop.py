#for loop:A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#ith the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
#Print each fruit in a fruit list:

Fruits = ['apple','banana','orange','strawberry']
for fruit in Fruits: #here fruit is variable
    print(fruit)

#The for loop does not require an indexing variable to set beforehand.
#looping through string
name = 'Manjunath Kandur'
for i in name:
    print(i)

#BREAK statement: With the break statement we can stop the loop before it has looped through all the items
furits = ['apple','banana','orange','strawberry']
for fruit in furits:
    print(fruit)
    if fruit == 'banana': #it breaks the loop at banana
        break

for fruit in furits:
    if fruit == 'banana': # here code break at apple because it reads banana before print
        break
    print(fruit)

#CONTINUE statement : With the continue statement we can stop the current iteration of the loop, and continue with the next

names = ['ck','gk','ak','mk','sk']
for name in names:
    if name == 'mk': #it skips mk
        continue
    print(name)

for name in names:
    print(name)
    if name == 'mk': continue #here it wont works as code prints mk before it comes to continue block

#range() function:
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

x = range(6)
for i in x: #here number start with 0 and ends with 5
    print(i)

#however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
y = range(2,6)
for i in y:
    print(i)

#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
z= range(2,30,3) #syntax range(start,stop,step) here it prints every 3rd integer
for i in z:
    print(i)

#Else in For Loop: The else keyword in a for loop specifies a block of code to be executed when the loop is finished

a = range(0,6)
for i in a:
    print(i)
else:
    print('finished')

# The else block will NOT be executed if the loop is stopped by a break statement
for i in a:
    print(i)
    if i == 4:
        break #here sequence break at 4 so no else statement is printed.
else:
    print('finished')

#Nested Loops: A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop":

x = ['c','g','a','s','m']
y = 'k'

for i in x:
    for j in y:
        print(i,j)

#pass Statement:if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
w = [1,2,3]
for i in w:
    pass

#enumerate(): Gives both the index and value.
Fruits = ['apple','banana','orange','strawberry']
for index,fruit in enumerate(Fruits):
    print(index,fruit)

#zip() : Loop through multiple lists together. its acts like nested loop
names = ['Ram', 'John', 'Mike']
ages = [20, 21, 22]

for name, age in zip(names, ages):
    print(name, age)

#Reverse Loop:
name = 'ram'
for i in name[::-1]: #with string
    print(i)

for i in names[::-1]: #with list
    print(i)

q = range(0,11)
for i in q[::-1]: #with range
    print(i)