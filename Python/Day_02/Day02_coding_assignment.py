#Print Personal Information
name = 'sk'
age = 19
city = 'Bng'
print(name)
print(age)
print(city)

#Two Numbers
a = 10
b = 16
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

#Swap two variables using a temporary variable
q = 6
w = 'mk'
h = q #store q in h
q = w #assign w to q
w = h #assign stored value to w
print(q,w)

#Swap two variables without a temporary variable.
q = 6
w = 'mk'
q,w = w,q
print(q,w)

#Find Square of a Number
a = 8
print(a**2)

#Find Cube of a Number
a = 7
print(a**3)

#Calculate Area of Rectangle Area = Length*Breadth
l = float(input(f'Enter the length of triangle: '))
b = float(input(f'Enter the Breadth of triangle: '))
a = l*b
print(f'Area of rectangle :{round(a,2)}')

#Calculate Perimeter of Rectangle P=2(l+b)
p = 2*(l+b)
print(f'perimeter of rectangle: {p}')

#Celsius to Fahrenheit Converter F=9/5*C+32
C = float(input(f'Enter the value of Celsius: '))
F = 9/5*C+32
print(f'Temperature: {F} fahrenheit')

#Calculate Simple Interest SI=100P×R×T/100
P = float(input(f'Enter the value of Principle amount: '))
R = float(input(f'Enter the value of Rate: '))
T = float(input(f'Enter the value of Time: '))
SI = P*T*R/100
print(f'simple intrest is {SI}')

#Percentage Calculator Percentage=obtained Marks/total Marks*100
OM = float(input(f'Enter the value of Obtained marks: '))
TM = 100
Percentage = OM/TM *100
print(f'your percentage is {Percentage}%')


#Find Remainder
a = 10
b = 4
print(a%b)

#Find Power of a Number
print(2**4)

#Convert Minutes to Seconds : Seconds = Minutes * 60
minutes = int(input(f'Enter the number of minutes: '))
seconds = minutes*60
print(f'minutes: {minutes} seconds: {seconds}')

#Convert Kilometers to Meters
kilometers = float(input(f'Enter the number of kilometers: '))
meters = kilometers*1000
print(f'kilometers: {kilometers} meters: {meters}')

#Mini Bill Calculator
product = input(f'enter the product name: ')
quantity = int(input(f'Enter the quantity: '))
price_per_item = float(input(f'Enter the price: '))
total_bill = quantity*price_per_item
print(f'total bill: {total_bill}')

#Compare two numbers using all comparison operators.
q = 8
w = 10
print(q==w)
print(q!=w)
print(q>w)
print(q<w)
print(q>=w)
print(q<=w)


# Mini challenge:
# Student Report Card Program
# Demonstrates:
# Variables
# User Input
# Type Casting
# Arithmetic Operators
# Comparison Operators
# Assignment Operators
# Logical Operators
# Equality Operators
# Formatted Output
# Comments
# ==========================================

# Taking user details
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Taking marks of 5 subjects
print("\nEnter marks out of 100")

sub1 = float(input("Subject 1: "))
sub2 = float(input("Subject 2: "))
sub3 = float(input("Subject 3: "))
sub4 = float(input("Subject 4: "))
sub5 = float(input("Subject 5: "))

# Calculating total marks
total = sub1 + sub2 + sub3 + sub4 + sub5

# Calculating percentage
percentage = (total / 500) * 100

# Converting percentage to integer
percentage_int = int(percentage)

# -------------------------
# Demonstrating Operators
# -------------------------

# Arithmetic Operator
average = total / 5

# Assignment Operator
bonus = 0
bonus += 5

# Comparison Operator
passed = percentage >= 35

# Equality Operator
is_hundred = percentage_int == 100

# Logical Operator
eligible_for_scholarship = percentage >= 90 and age <= 25

# -------------------------
# Printing Report
# -------------------------

print("\n" + "=" * 40)
print("          STUDENT REPORT")
print("=" * 40)

print(f"Name              : {name}")
print(f"Age               : {age}")

print("\nMarks")
print(f"Subject 1         : {sub1}")
print(f"Subject 2         : {sub2}")
print(f"Subject 3         : {sub3}")
print(f"Subject 4         : {sub4}")
print(f"Subject 5         : {sub5}")

print("\nResults")
print(f"Total Marks       : {total}/500")
print(f"Average Marks     : {average:.2f}")
print(f"Percentage        : {percentage:.2f}%")
print(f"Integer Percentage: {percentage_int}%")

print("\nOperator Demonstration")
print(f"Bonus Marks (+ =)             : {bonus}")
print(f"Passed (>= 35%)               : {passed}")
print(f"Perfect Score (== 100%)       : {is_hundred}")
print(f"Scholarship Eligible (and)    : {eligible_for_scholarship}")

print("=" * 40)
print("Thank you!")
print("=" * 40)