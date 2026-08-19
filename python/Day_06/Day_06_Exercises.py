#Practice 1: Student Marks Program
s1 = float(input('enter s1 marks: ')) #user marks input
s2 = float(input('enter s2 marks: '))
s3 = float(input('enter s3 marks: '))
s4 = float(input('enter s4 marks: '))
s5 = float(input('enter s5 marks: '))

marks = list((s1,s2,s3,s4,s5)) #converting marks into list
print(f'marks: {marks}')

print(f'highest marks: {max(marks)}')
print(f'lowest marks: {min(marks)}')

average = sum(marks)/len(marks)
print(f'average marks: {average:.2f}')

#Practice 2: Shopping List Program
shopping = []

shopping.append('bread')
shopping.append('butter')
shopping.append('carrot')
shopping.append('chicken')
shopping.append('oil')

print(f'shopping list: {shopping}')

shopping.remove('butter')

print(f'updated shopping list: {shopping}')

shopping.insert(0,'cream')

print(f'updated shopping list: {shopping}')

shopping.pop(0)

print(f'updated shopping list: {shopping}')

shopping.clear()
print(f'updated shopping list: {shopping}')

#Practice 3: Find Maximum and Minimum(using loop)
s1 = float(input('enter s1 marks: ')) #user marks input
s2 = float(input('enter s2 marks: '))
s3 = float(input('enter s3 marks: '))
s4 = float(input('enter s4 marks: '))
s5 = float(input('enter s5 marks: '))

marks = list((s1,s2,s3,s4,s5)) #converting marks into list
print(f'marks: {marks}')

highest = marks[0]
lowest = marks[0]

for i in marks: #highest marks
    if i > highest:
        highest = i
print(f'highest mark: {highest}')

for i in marks:
    if i < lowest:
        lowest = i
print(f'lowest mark: {lowest}')

#Create a list of 10 numbers and print only even numbers.
list1 = [1,3,4,5,6,7,8,9,10,12]
even = []
for i in list1:
    if i % 2 == 0:
        even.append(i)
print(f'even numbers: {even}')

#Create a list of names and sort them alphabetically.
list2 = ['banana','apple','grapes','carrot']
list2.sort()
print(list2)

#Reverse a list without using reverse().
list2 = ['banana','apple','grapes','carrot']

print(list2[::-1])

#Count how many times a number appears in a list.
list3 = [1, 2, 3, 2, 4, 1, 5, 6]

num = int(input("Enter a number: "))
count = 0

for i in list3:
    if i == num:
        count += 1

print(f"{num} appears {count} time(s).")

#Remove duplicate values from a list.
list3 = [1,2,3,2,4,1,5,6]
unique = []

for i in list3:
    if i not in unique:
        unique.append(i)

print(unique)

#Find the second largest number in a list.
list3 = [1, 2, 6, 6, 5]

unique = list(set(list3))
unique.sort()

print(unique[-2])