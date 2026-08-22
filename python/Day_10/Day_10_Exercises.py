#Practice 1 — Grade Calculator
marks = float(input("Enter the marks: "))

if marks >= 95:
    print("Your grade is A+")
elif marks >=90:
    print("Your grade is A")
elif marks >=85:
    print("Your grade is B+")
elif marks >= 80:
    print("Your grade is B")
elif marks >=75:
    print("Your grade is C+")
elif marks >=70:
    print("Your grade is C")
elif marks >=65:
    print("Your grade is D+")
elif marks >=60:
    print("Your grade is D")
else:
    print('you are failed')

#Practice 2 — Age Eligibility
age = int(input("Enter your age: "))

if age >= 65:
    print('you are senior citizen')
elif age >= 18:
    print('you are adult')
else:
    print('you are minor')

#Practice 3 — Login System
username = input("Enter your username: ").lower()
password = input("Enter your password: ").lower()

if username == "admin" and password == "python1234":
    print("Welcome " + username + "!")
else:
    print('please check username/password')

#Practice 4 — Salary Catego
salary = int(input("Enter salary: "))

if salary >= 100000:
    print("High Income")
elif salary >= 50000:
    print("Middle Income")
elif salary >= 25000:
    print("Lower Middle")
else:
    print("Entry Level")

#-----------------------------------------------------------------------------------------------------------------------

#Check whether a number is positive, negative, or zero.

num = float(input("Enter a number: "))

if num > 0:
    print("Your number is positive")
elif num < 0:
    print("Your number is negative")
else:
    print("Your number is zero")

#Find the largest of two numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

list1 = [num1, num2]

largest = max(list1)
print(largest)

#or

largest = list1[0]

for i in list1:
    if i > largest:
        largest = i
print(largest)

#Check whether a year is a leap year.
year = int(input("Enter year: "))

if year % 400 == 0:
    print(year, "is a leap year")
elif year % 100 == 0:
    print(year, "is not a leap year")
elif year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#Create a BMI category checker.
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / (height ** 2)

print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


#Password strength checker.
password = input("Enter password: ")

has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(not ch.isalnum() for ch in password)

if len(password) < 8:
    print("Weak Password - Must be at least 8 characters")

elif has_upper and has_lower and has_digit and has_special:
    print("Strong Password")

elif (has_upper and has_lower) or (has_lower and has_digit):
    print("Medium Password")

else:
    print("Weak Password")