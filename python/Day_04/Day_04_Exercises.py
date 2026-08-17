#Practice 1 — Calculator
n1 = float(input("Enter a number: "))
n2 = float(input("Enter another number: "))

sum = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
fdiv= n1 // n2

print(f'Addition : {sum}')
print(f'Subtraction : {sub}')
print(f'multiplication : {mul}')
print(f'division : {div}')
print(f'Float division : {fdiv}')

#Practice 2 — Percentage Calculator
s1 = float(input('enter s1 marks: '))
s2 = float(input('enter s2 marks: '))
s3 = float(input('enter s3 marks: '))
s4 = float(input('enter s4 marks: '))
s5 = float(input('enter s5 marks: '))

total = s1 + s2 + s3 + s4 + s5
average = total / 5
percentage = (total / 500) * 100

print('----- STUDENT REPORT -----')
print(f'total marks: {total}')
print(f'average marks: {average}')
print(f'percentage marks: {percentage}')

#Practice 3 — Eligibility Checker(Age ≥ 18 and percentage >= 60)]
age = int(input('enter age: '))
percentage = float(input('enter percentage: '))

if age >= 18 and percentage >=60:
    print('eligible')
else:
    print('not eligible')

#Find remainder of two numbers.
num1 = float(input('enter first number: '))
num2 = float(input('enter second number: '))

print(n1%n2)

#Calculate square of a number
num = float(input('enter a number: '))
print(num**2)

#Check if a number is even.
num = int(input('enter a number: '))

if num%2 == 0:
    print('even')
else:
    print('odd')

#Compare two lists using == and is.
l1 = [1,2,3,4]
l2 = [1,2,3,4]

print(l1 == l2)
print(l1 is l2)

#Build a simple EMI calculator using arithmetic operators.
# 1. Inputs
principal = float(input("Enter principal loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
tenure_years = int(input("Enter tenure in years: "))

# 2. Conversions
# Monthly interest rate
monthly_rate = annual_rate / (12 * 100)

# Total number of monthly installments
months = tenure_years * 12

# 3. EMI Calculation using Basic Arithmetic Operators
# Using ** for exponentiation, * for multiplication, / for division
numerator = principal * monthly_rate * ((1 + monthly_rate) ** months)
denominator = ((1 + monthly_rate) ** months) - 1

emi = numerator / denominator

# 4. Summary Calculations
total_payment = emi * months
total_interest = total_payment - principal

# 5. Output
print("\n--- Loan Summary ---")
print(f"Monthly EMI:        ₹{emi:,.2f}")
print(f"Total Interest:     ₹{total_interest:,.2f}")
print(f"Total Amount Payable: ₹{total_payment:,.2f}")

# Weekend Mini Project — Student Marks Calculator

try:
    # Inputs
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    s1 = float(input('Enter s1 marks: '))
    s2 = float(input('Enter s2 marks: '))
    s3 = float(input('Enter s3 marks: '))
    s4 = float(input('Enter s4 marks: '))
    s5 = float(input('Enter s5 marks: '))

    # Calculations
    total = s1 + s2 + s3 + s4 + s5
    average = total / 5
    percentage = (total / 500) * 100

    # Display Student Info & Summary
    print('\n----- STUDENT REPORT -----')
    print(f'Name:             {name}')
    print(f'Age:              {age}')
    print(f'Total Marks:      {total:.2f} / 500')
    print(f'Average Marks:    {average:.2f}')
    print(f'Percentage:       {percentage:.2f}%')

    # Grade & Pass/Fail Status
    if percentage > 100 or percentage < 0:
        print("Status:           Invalid marks entered!")
    else:
        # Grade Determination
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        # Pass/Fail Determination
        status = "PASSED" if percentage >= 35 else "FAILED"

        print(f'Grade:            {grade}')
        print(f'Status:           {status}')

except ValueError:
    print("\nInvalid input! Please enter valid numerical values for age and marks.")