#Take two numbers and print their sum, difference, product and division.
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

n1 = float(input('enter n1: '))
n2 = float(input('enter n2: '))

addition = add(n1,n2)
subtraction = sub(n1,n2)
multiplication = mul(n1,n2)
division = div(n1,n2)

print(f'addition: {addition}')
print(f'subtraction: {subtraction}')
print(f'multiplication: {multiplication}')
print(f'division: {division}')

#Take a user's name and age and print:
def intro(name, age):
    print(f'Hello {name}, you are {age} years old')


name = input('Enter your name: ')
age = int(input('Enter your age: '))

intro(name, age)

#Convert Celsius to Fahrenheit.
def temp(num):
    return (num * 9/5)+32

temperature = float(input('Enter temperature: '))


result = temp(temperature)
print(result)

#Calculate the area of a circle.
radius = float(input('Enter radius: '))

area = 3.14 * radius**2
print(area)

#Take marks for 5 subjects and calculate total and percentage.
s1 = float(input('enter s1 marks: '))
s2 = float(input('enter s2 marks: '))
s3 = float(input('enter s3 marks: '))
s4 = float(input('enter s4 marks: '))
s5 = float(input('enter s5 marks: '))

total_marks = s1 + s2 + s3 + s4 + s5
percentage = (total_marks / 500) * 100

print('-----student report-----')
print('The total marks is', total_marks)
print(f'The percentage is {percentage:.2f}')

#Reverse a string without using [::-1]
user = input('Enter a word: ')

print(''.join(reversed(user)))

#Check whether a string is a palindrome.
user = input('Enter a word: ')

if user == user[::-1]:
    print('its palindrome')
else:
    print('not palindrome')

#Count vowels in a string.
user = input('Enter a word: ')

count = 0

for i in user:
    if i in 'aeiouAEIOU':
        count += 1
print(count)

#Count uppercase, lowercase and digits in a string.
user = input('Enter a word: ')

upper_case = 0
lower_case = 0
digits = 0

for i in user:
    if i.isupper():
        upper_case += 1
    elif i.islower():
        lower_case += 1
    elif i.isdigit():
        digits += 1
    else:
        pass

print(f'upper case: {upper_case}')
print(f'lower case: {lower_case}')
print(f'digits: {digits}')

#Remove spaces from a string.
user = input('Enter a word: ')

print(user.strip())

#Find the largest number in a list without using max().
list1 = [32,89,56,87.65,78]

largest_num = 0

for i in list1:
    if i > largest_num:
        largest_num = i
print(largest_num)


#Find the smallest number without using min().
list1 = [32,89,56,87,65,78]

smallest_num = int(list1[0])

for i in list1:
    if i < smallest_num:
        smallest_num = i
print(smallest_num)

#Calculate the sum of all numbers in a list without using sum().
list1 = [32,89,56,87,65,78]

total = 0

for i in list1:
    total += i

print(total)

#Remove duplicate values from a list.
list1 = [32,89,56,87,65,78,32,89]

unique_list = list(set(list1))
print(unique_list)

#or

unique_list = []

for i in list1:
    if i not in unique_list:
        unique_list.append(i)
    else:
        pass

print(unique_list)

#Given a list of student marks, calculate:
marks = [78, 45, 89, 32, 67, 91, 55]

highest = marks[0]
lowest = marks[0]
total = 0
passed = 0

for mark in marks:

    # Find highest
    if mark > highest:
        highest = mark

    # Find lowest
    if mark < lowest:
        lowest = mark

    # Calculate total
    total += mark

    # Count passed students
    if mark >= 40:
        passed += 1

average = total / len(marks)

print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Average:", average)
print("Students passed:", passed)

#Check whether a number is even or odd.
user = int(input("Enter a number: "))

if user % 2 == 0:
    print('even')
else:
    print('odd')

#Check whether a number is prime.
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")

#Print the multiplication table of a number.
user = int(input("Enter a number: "))

for i in range(1,11):
    print(f'{user} * {i} = {user * i}')

#Print this pattern:(triangle)
for i in range(1,6):
    for j in range(i):
        print("*",end='')
    print()

rows = 5

for i in range(rows):
    for j in range(rows-i-1):
        print(' ',end='')

    for j in range(2*i+1):
        print('*',end='')

    print()

#Create a function that returns the largest of three numbers.
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


result = largest(25, 48, 32)

print("Largest number:", result)

#Create a function that accepts any number of arguments using *args and returns their average.
def avg(*nums):
    return sum(nums) / len(nums)

result = avg(25, 48, 32)
print("Average number:", result)

#Create a lambda function to calculate the square of a number.
x = lambda a: a**2

print(x(2))

#second largest number
num = [27,87,98,76,45,27,46,50,56]

largest_num = 0
second_largest_num = 0

for i in num:
    if i > largest_num:
        second_largest_num = largest_num
        largest_num = i

print(second_largest_num)
