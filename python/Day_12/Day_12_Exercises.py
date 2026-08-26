#BMI Calculator
def bmi(weight,height):
    return weight / (height * height)

result = bmi(62,1.20)
print(result)

#Math Utility Functions: Create several reusable functions.

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def sqr(a):
    return a ** 2

def cube(a):
    return a ** 3

print(add(10,4))
print(sub(10,4))
print(mul(10,4))
print(div(10,4))
print(sqr(10))
print(cube(3))

#Say hello
def greet(name,greet='hello'):
    print(f'{greet} {name}')
greet('john')

#Check whether a number is even / odd

def even_odd(n):
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'
print(even_odd(4))

#Find the largest of two numbers

def my_f(a,b):
    if a > b:
        return f'{a} is largest number between {a} and {b}'
    else:
        return f'{b} is largest number between {a} and {b}'

print(my_f(4,5))

#Find the smallest of two numbers

def my_s(a,b):
    if a<b:
        return f'{a} is smaller than {b}'
    else:
        return f'{b} is smaller than {a}'

print(my_s(5,8))

#Calculate the average of three numbers

def avg(*arg):
    return sum(arg) / len(arg)
print(avg(4,6,7))


#Create a calculator using functions
# Function definitions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

# Main program
print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print("Result:", add(num1, num2))
elif choice == "2":
    print("Result:", subtract(num1, num2))
elif choice == "3":
    print("Result:", multiply(num1, num2))
elif choice == "4":
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice!")

#Create a student marks calculator
def total(*arg):
    return sum(arg)

def avg(*arg):
    return sum(arg) / len(arg)

def per(obtained,total):
    return (obtained / total) * 100

print('---- REPORT CARD-----')

s1 = float(input('enter s1 marks: '))
s2 = float(input('enter s2 marks: '))
s3 = float(input('enter s3 marks: '))
s4 = float(input('enter s4 marks: '))
s5 = float(input('enter s5 marks: '))

marks = (s1, s2, s3, s4, s5)
total_marks = total(*marks)
average = avg(*marks)
percentage = per(total_marks, 500)
grade = 0

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    garage = 'F'

print('----- student report -----')
print(f'total_marks : {total_marks}')
print(f'average : {average}')
print(f'percentage : {percentage}')
print(f'grade : {grade}')

