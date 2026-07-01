#Print the length of a string.
user = input(f'enter your name: ')
print(len(user))

#Convert a string to uppercase.
a = 'hello'
print(a.upper())

#Convert a string to lowercase.
b = 'HELLO'
print(b.lower())

#Print First Character
c = 'hello world'
print(c[0])

#Reverse a String
print(user[::-1])

#Convert to Title Case
print(user.title())

#Count Characters
print(len(user))

#Remove Extra Spaces
e =' hey '
print(e.strip())

#Replace a Word
print(e.replace('h','H'))

#Extract First 5 Characters
W = 'HELLO WORLD'
print(W[:6])

#Extract Last 4 Characters
print(W[-4:])

#Email Formatter
email = input(f'enter your email: ')
username,domain = email.split('@')
print(f'username : {username}')
print(f'domain: {domain}')

#Count Occurrences of a Character
t = 'hello world'
print(t.count('o'))

#Display Initials
name = input(f'eneter your name: ')
firstname,lastname = name.split(' ')
print(firstname[0]+lastname[0])

#Create a program that takes a full name and prints
print(name) #original name
print(name.upper()) #upper case
print(name.lower()) #lower case
print(name.title()) #title
print(len(name))
print(name[::-1])

#Write a program to input a string and print each character on a new line.
q = 'Hello, python!'
for i in q:
    print(i)

#Write a program to check whether a given string is a palindrome.
if q == q[::-1]:
    print('it\'s palindrome')
else:
    print('it\'s not palindrome')

#Write a program to count the number of vowels in a string.
s = 'hello world'
count = 0

for i in s:
    if i in 'aeiouAEIOU':
        count += 1
print(count)

#Write a program to count the number of consonants in a string.
s = 'hello world'
count = 0

for i in s:
    if i.isalpha() and i not in 'aeiouAEIOU':
        count += 1
print(count)

#Write a program to print every second character from a string.
s = 'hello world'
print(s[::2])

#Check whether two strings are equal.
str1 = input('Enter a string: ')
str2 = input('Enter another string: ')

if len(str1) == len(str2):
    print('both strings are equal')
else:
    print('strings are not equal')

#Count the number of words in a sentence.
str = input('enter a string')
str = str.split(' ')
count = 0
for i in str:
    if i.isalpha():
        count += 1
print(count)

#Find the middle character of a string.
text = "kandur"

middle = len(text) // 2

print(text[middle])

text = "kandur"

for i in range(len(text)):
    if i == len(text) // 2:
        print(text[i])

#Remove all vowels from a string.
text = "kandur"
result =''

for i in text:
    if i.lower() not in 'aeiou':
        result += i
print(result)