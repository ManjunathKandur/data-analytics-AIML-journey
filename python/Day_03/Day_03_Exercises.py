#Practice Program 1 — Age Calculator

current_year = 2026

user_bod = int(input("Enter your birth year: "))

age = current_year - user_bod

print("Your age is:", age)

#Practice Program 2 — Temperature Converter(Celsius → Fahrenheit)

celsius = float(input("Enter your temperature in celsius: "))

fahrenheit = 9/5 * celsius + 32

print("Fahrenheit:", fahrenheit)

#Practice Program 3 — Marks Calculator: Take marks of 5 subjects and calculate total, average, and percentage.
s1 = float(input('Maths: '))
s2 = float(input('English: '))
s3 = float(input('Social: '))
s4 = float(input('Computer: '))
s5 = float(input('Science: '))

total = s1 + s2 + s3 + s4 + s5
average = total / 5
percentage = (total/500) * 100

print('\n ----- STUDENT REPORT ----- ')
print('total marks obtained: ', total)
print('average marks obtained: ', average)
print('percentage obtained: ', percentage)


