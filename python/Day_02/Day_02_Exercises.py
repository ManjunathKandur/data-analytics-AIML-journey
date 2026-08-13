#Create 5 variables of different datatypes.
a = 'mk' #str
b = 1 #int
c = 1.0 #float
d = True #bool
e = ['mk',1,2] #list

#Convert "500" into an integer.
num = '500'
num_1 = int(num)
print(type(num),type(num_1))

#Convert 75 into a float.
num = 75
num_2 = float(num)
print(num_2)
print(type(num),type(num_2))

#Convert 99.99 into an integer.
num = 99.99
num_3 = int(num)
print(num_3)
print(type(num),type(num_3))

#Convert your age into a string and print: "I am 23 years old".
age = 23
age = str(age)
print(type(age))
print('I am', age, 'years old')
print('I am'+age+'years old')
print(f'I am {age} years old')

#Check the datatype of None.
x = None
print(type(x))

#Create a Boolean variable for is_employed.
is_employed = False
print(type(is_employed))

#Convert 0, 1, "", and "AI" into booleans.
a = bool(0)
b = bool(1)
c = bool('')
d = bool('Ai')
print(a, b, c, d)

#Take a number as input and convert it to float.
num = input('enter a number: ')
num = float(num)
print(type(num))
#or
num_4 = float(input('enter a number: '))
print(type(num_4))

#-----------------------------------------------------------------------------------------------------------------------

#Mini Task — Student Information Program

print('========================= STUDENT INFORMATION =========================')

name = input('enter your name: ')
age = int(input('enter your age: '))
percentage = float(input('enter your percentage: '))
graduated = input("Graduated? (True/False): ")

graduated = graduated == True

print("\n------ REPORT ------")

print("Name:", name)
print("Age:", age)
print("Percentage:", percentage)
print("Graduated:", graduated)

print('\n------ Data types ------')
print(type(name))
print(type(age))
print(type(percentage))
print(type(graduated))