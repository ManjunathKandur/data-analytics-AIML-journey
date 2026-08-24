#Print numbers from 1 to 100.

i = 0
while i <= 100:
    print(i,end=' ')
    i = i + 1

print () #it prints next outcome in coming lines

#Print all even numbers from 1 to 50.
i = 0
even = []
while i <= 50:
    if i % 2 == 0:
        even.append(i)
    i = i + 1
print(even)

#Print all odd numbers from 1 to 50.
odd =[]
for i in range(1,51):
    if i % 2 != 0:
        odd.append(i)
print(odd)

#Find the sum of numbers from 1 to n
n = 50
sum = 0

for i in range(1,n+1):
    sum = sum + i
print(sum)

#Find the factorial of a number.
n = 6
fact = 1
for i in range(1,n+1):
    fact *=i
print(fact)

#Print the multiplication table of a given number.
n = 2

for i in range(1,11):
    print(f'{n} * {i} = {n*i}')

#Count the number of digits in a number.
num = 34567

count = 0

while num != 0:
    num = num // 10
    count += 1

print("Number of digits:", count)

#Reverse a number.
num = 34567
reverse = 0

while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)

#Find the sum of digits of a number.
num = 34567
total = 0

while num != 0:
    digit = num % 10 #get last digit
    total = total + digit
    num = num // 10 #remove last digit

print(total)

#Count how many numbers between 1 and 100 are divisible by 3.
count = 0

for i in range(1,101):
    if i % 3 == 0:
        count += 1

print(count)

#Check whether a number is prime.
num = int(input('number: '))
count = 0

for i in (1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print('yes')
else:
    print('no')

#Print all prime numbers between 1 and 100.
count_prime = 0

for num in range(2, 101):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        count_prime += 1

print(count_prime)

#Keep accepting numbers until the user enters 0
i = int(input('number: '))

while i != 0:
    print(i)
    i = int(input('number: '))

#Find whether a number is a palindrome.
num = 23452
reverse = 0
while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print(reverse)

if num == reverse:
    print('palindrome')
else:
    print('not palindrome')

#Count vowels in a string using a loop.
string = 'i love python'

count = 0

for i in string:
    if i in 'aeiouAEIOU':
        count += 1
print(count)

#Find character frequency in a string using loops.
string = 'i love python'

dict1 = {}

for i in string:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

print(dict1)