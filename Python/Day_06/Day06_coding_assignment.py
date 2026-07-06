#Practice Project 1: Login System
user_name = input("Enter user_name: ").lower()
user_password = input("Enter user_password: ")
if user_name == 'admin' and user_password == '1234':
    print('you are successfully logged in')
else:
    print('you are not successfully logged in')


#Practice Project 2: Grade Calculator
marks = float(input("Enter marks: "))
if marks >= 90.00:
    print(f'your marks: {marks} and your grade A')
elif marks >= 75.00:
    print(f'your marks: {marks} and your grade B')
elif marks >= 50.00:
    print(f'your marks: {marks} and your grade C')
elif marks >= 35.00:
    print(f'your marks: {marks} and your grade D')
else:
    print(f'your marks: {marks} and your failed')

#Practice Project 3: Shopping Bill Generator
amount = float(input("Enter bill amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
else:
    discount = 0

final_bill = amount - discount

print("Discount:", discount)
print("Final Bill:", final_bill)

#Check whether a number is positive or negative.
number = int(input("Enter a number: "))
if number > 0:
    print(f'the {number} is positive')
elif number < 0:
    print(f'the {number} is negative')

#Check whether a number is even or odd.
if number % 2 == 0:
    print(f'the {number} is even')
else:
    print(f'the {number} is odd')

#Check if a person is eligible to vote.
user_age = int(input("Enter your age: "))
if user_age > 18:
    print('you can cast your vote')
else:
    print('you are not allowed to cast your vote')

#Find the larger of two numbers.
n1 = float(input("Enter n1: "))
n2 = float(input("Enter n2: "))

if n1 > n2:
    print(f'{n1} is larger number')
elif n2 > n1:
    print(f'{n2} is larger number')
else:
    print(f'both {n1} and {n2} are equal')

#Check whether a year is a leap year.
year = int(input("Enter a year: "))

if year % 4 == 0:
    print("Leap year")
else:
    print("Non leap year")

#Find the Largest of Three Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)

#Electricity bill calculator.
number_of_units = float(input("Enter number of units: "))
price_per_unit = 2.86
bill = price_per_unit * number_of_units
tax = 0.018 * bill

final_bill = tax + bill
if number_of_units < 200:
    print(f'Electricity is free')
elif number_of_units >= 200 and number_of_units < 500:
    print(f'your electricity bill is {final_bill}')
else:
    print(f'your electricity bill is {final_bill+100}')