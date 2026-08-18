#Practice 1 — Reverse String
name = 'Martin'
reverse = name[::-1]
print(reverse)

#Practice 2 — Palindrome Checker
user = input('enter a word: ')

if user == user[::-1]:
    print('Palindrome')
else:
    print('Not a palindrome')

#Practice 3 — Count Characters
user = input('enter a word: ')
count = 0

for i in user:
    count += 1

print(count)

#or
print(len(user))

#Practice 4 — Email Formatter
email = input('enter a email: ')

clean = email.strip().lower()
print(clean)

#Mini Challenge

name = input('enter a name: ')
email = input('enter a email: ')
city = input('enter a city: ')

name = name.title()
email = email.strip().lower()
city = city.title()

print('---------------------')
print('\n  USER PROFILE     ')
print('\n-------------------')
print(f'Name: {name}')
print(f'Email: {email}')
print(f'City: {city}')
print('\n-------------------')

#count number word in sentence.
user = input('enter a sentence: ')
list1 = user.split()
print(list1)
print(len(list1))

#Problem 1 — Name Formatter
name = input("What is your name? ")

name = name.strip().title()

print(f"Hello {name}!")

#Problem 2 — Username Generator:
full_name = input("Enter your full name: ") # Input full name and birth year
birth_year = input("Enter your birth year: ")

first_name = full_name.split()[0].lower() # Get the first name, convert to lowercase

last_two_digits = birth_year[-2:] # Get the last two digits of the birth year using string indexing

username = first_name + last_two_digits # Combine to create username

print(username)

#Problem 3 — Password Strength Checker:
password = input("Enter password: ")

length_valid = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)

if length_valid and has_digit and has_upper and has_lower:
    print("Strong Password")
else:
    print("Weak Password")