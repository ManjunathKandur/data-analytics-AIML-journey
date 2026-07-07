#Print numbers from 1 to 100.
a = range(1,101)
for i in a:
    print(i)

#Print only even numbers from 1 to 50.
a = range(1,51)
for i in a:
    if i % 2 == 0:
        print(i)

#Print only odd numbers from 1 to 50.
a = range(1,50)
for i in a:
    if i % 2 != 0:
        print(i)

#Calculate the sum of numbers from 1 to 100.
a = range(1,101)
total = 0
for i in a:
    total = total + i
print(total)

#Print a multiplication table for any number.
num = 2
for i in range(1,11):
    print(f'{num}*{i} = {num*i}')

#Count vowels in a string using a for loop.
name = 'Manjunath Kandur'
count = 0
for i in name:
    if i in 'aeiouAEIOU':
        count += 1
print(count)

#Reverse a string using a for loop.
for i in name[::-1]:
    print(i)

#Find the largest number in a list.
numbers = [3, 7, 2, 9, 4, 1]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print(largest)

#Find the smallest number in a list
numbers = [3, 7, 2, 9, 4, 1]
smallest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i
print(smallest)

#print patern:
for i in range(1, 6):
    print("*" * i)

for i in range(5,0,-1):
    print("*" * i)

#Print numbers from 1 to 20.
i = 1
while i <=20:
    print(i)
    i = i + 1

#Print numbers from 20 to 1.
i = 20
while i >=1:
    print(i)
    i = i - 1

#Print even numbers from 1 to 50.
i = 1
while i <=50:
    if i % 2 == 0:
        print(i)
    i = i + 1

#Print odd numbers from 1 to 50.
i = 1
while i <=50:
    if i % 2 != 0:
        print(i)
    i = i + 1

#Find the sum of numbers from 1 to 100.
i = 0
total = 0
while i <=100:
    total = total + i
    i = i + 1
print(total)

#Print the multiplication table of a given number.
num = 3
i = 1
while i <=10:
    print(f"{num} x {i} = {num * i}")
    i = i + 1

#Count the number of digits in a number.
num = 6789
count = 0

while num > 0:
    num = num//10
    count += 1
print(count)

#Reverse a number.
num = 5432

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)

#Check whether a number is a palindrome.
num = 5432

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if num == reverse:
    print('palindrome')
else:
    print('not palindrome')

#Guess the secret number.
num = 8
user = int(input('Enter a number between 1 and 10: '))

while user != num:
    print('Try again')
    user = int(input('Enter a number between 1 and 10: '))

print('Correct number!')

#Print multiplication tables from 1 to 10.

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j}')

#Find the largest digit in a number.
num = input("Enter a number: ")

largest = 0

for digit in num:
    if int(digit) > largest:
        largest = int(digit)

print("Largest digit:", largest)

#Print a square star (*) pattern.
for i in range(1,6):
    print("* "*i)

#Print a right triangle star pattern.
rows = 5

for i in range(rows):
    print(" "*(rows-i-1), "*"*(2*i+1))