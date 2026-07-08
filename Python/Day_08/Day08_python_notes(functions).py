#Python Functions:
#                 A function is a block of code which only runs when it is called.
#                 A function can return data as a result.
#                 A function helps avoiding code repetition.

#Creating a Function:
#In Python, a function is defined using the def keyword, followed by a function name and parentheses:
def my_function(): #This creates a function named my_function that prints "Hello" when called.
    print('hello')
my_function() #To call a function, write its name followed by parentheses

my_function() #You can call the same function multiple times
my_function()
my_function()

#------------------------------------------------------------------------------------------------------------------------------------------

#Function Names:
#               A function name must start with a letter or underscore
#               A function name can only contain letters, numbers, and underscores
#               Function names are case-sensitive (myFunction and myfunction are different)
#               eg: calculate_sum() , _private_function() , myFunction2()

#------------------------------------------------------------------------------------------------------------------------------------------

#Return Values:
#              Functions can send data back to the code that called them using the return statement.
#              When a function reaches a return statement, it stops executing and sends the result back

def my_function2():
    return 'mk'
message = my_function2()
print(message)
# or
print(my_function2()) #you can directly use function itself

#------------------------------------------------------------------------------------------------------------------------------------------

#The pass Statement:
#            Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement

def my_function3():
    pass

#-----------------------------------------------------------------------------------------------------------------------------------------

#Python Function Arguments:
#Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
#The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

def name(fname): #here fname is parameter
    print(f'{fname} Arora')

name('Sejal') #sejal is argument
name('Mukesh')
name('Rajesh')

#OR

def name2(fname):
    return f'{fname} Arora'

print(name2('Sejal'))
print(name2('Mukesh'))
print(name2('Rajesh'))

#Parameters vs Arguments:
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the actual value that is sent to the function when it is called.

#Number of Arguments:
#By default, a function must be called with the correct number of arguments.
#If your function expects 2 arguments, you must call it with exactly 2 arguments

def name3(fname,lname):
    print(f'{fname} {lname}')

name3('Raju','Desai')
name3('Sameer','Chaoudry')

#Default Parameter Values:
#You can assign default values to parameters. If the function is called without an argument, it uses the default value:

def countries(country = 'India'):
    print(f'I am from {country}')

countries('Sweden')
countries('Brazil')
countries() # here without arg soi used default value as india

#Keyword Arguments:
#You can send arguments with the key = value syntax.

def pet(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

pet(animal = "dog", name = "Buddy")
pet(name = 'Rocky', animal = 'Cat') #This way, with keyword arguments, the order of the arguments does not matter.

#Positional Arguments:
#When you call a function with arguments without using keywords, they are called positional arguments.
#Positional arguments must be in the correct order:

def pet(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

pet('Fish','Goldy')
pet('peeto','cow') #The order matters with positional arguments

#Mixing Positional and Keyword Arguments:
#You can mix positional and keyword arguments in a function call.
#However, positional arguments must come before keyword arguments:
def pet2(animal, name, age):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
  print("My", animal + "'s age is", age)

pet2('dog', age = 5 , name = 'Buddy')
#pet2(age = 1,name = 'goldy', 'fish') #this will lead to error as positional arg should come before keyarg.

#-----------------------------------------------------------------------------------------------------------------------------------------

#Passing Different Data Types:
#You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
#The data type will be preserved inside the function:

def fruit(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ['apple', 'banana', 'orange']
fruit(my_fruits)

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

#-------------------------------------------------------------------------------------------------------------------------------------
#Return Values:
#Functions can return values using the return statement:

def sum(x,y):
    return x + y

print(sum(10, 20))
#or
addition = sum(20,30)
print(addition)

def name(fullname):
    return f'Hello {fullname}'
print(name('Emil'))

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#Positional-Only Arguments:
#To specify positional-only arguments, add , / after the arguments:
def name(fname,/):
     print(f'Hello {fname}')

name('Rakesh')
#name(fname = 'mukesh') #key arg in this condition leads error

#Keyword-Only Arguments:
#To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")


#Combining Positional-Only and Keyword-Only:
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)