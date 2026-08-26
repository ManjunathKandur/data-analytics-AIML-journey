#Python Functions: A function is a block of code which only runs when it is called.
#                  A function can return data as a result.
#                  A function helps avoiding code repetition.


#Creating a Function:
def my_func(): #def(define) function_name():
    print('Hello World') #code

#Calling a Function: To call a function, write function name followed by parentheses:

my_func() #calling my_func

#You can call the same function multiple times:
my_func()
my_func()
my_func()

#Return Values: Functions can send data back to the code that called them using the return statement
#               If a function doesn't have a return statement, it returns None by default.
def my_func2():
    return 'Hello'

print(my_func2())

result = my_func2() #you can store function n variable and call.
print(result)

#If a function doesn't have a return statement, it returns None by default.
def my_func3():
    return

print(my_func3())

#The pass Statement: Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement.

def my_func4():
    pass

print(my_func4())


#-----------------------------------------------------------------------------------------------------------------------


#Python Function Arguments:
''' Arguments are specified after the function name, inside the parentheses.
ou can add as many arguments as you want, just separate them with a comma.'''

def greet(name):
    print(f'hello {name}')

greet('John') #here name is parameter and 'john' is argument

#Number of Arguments:
'''By default, a function must be called with the correct number of arguments.
If your function expects 2 arguments, you must call it with exactly 2 arguments.'''

def full_name(first_name, last_name):
    print(f'Hello {first_name} {last_name}')

full_name('John', 'Doe')
'''full_name('john')''' #it leads and error because only one argument was given

#Default Parameter Values:
'''You can assign default values to parameters. If the function is called without an argument, it uses the default value:'''
def user(name, city='New York'):
    print(f'Hello {name} from {city}')

user('john') #here city name prints as new york without calling as its set default.
user('Edwin','Landon') #but u can always change default parameter by calling different argument or value in this case city name landon


#Keyword Arguments:
'''You can send arguments with the key = value syntax.'''
'''This way, with keyword arguments, the order of the arguments does not matter.'''

def intro(name, age , city):
    print(f'hey i\'m {name} from {city} and {age} years old')

intro(name='John', age=30, city='New York')
intro(age=30, city='Landon', name='Edwin') #it does not matter order of argument as we calling with key(=)

#Positional Arguments:
'''When you call a function with arguments without using keywords, they are called positional arguments.'''
'''Positional arguments must be in the correct order.'''

def pet(animal,name):
    print(f'i have a {animal} and its name is {name}')

pet('dog','doggy')
pet('buno','cat') #here its not matches as buno is name and cat is animal but positions are wrong so output worng.

#Mixing Positional and Keyword Arguments:
'''You can mix positional and keyword arguments in a function call.
However, positional arguments must come before keyword arguments.'''

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)
'''my_function(name = "Buddy", age = 5,'cat')''' #it will leads to error as positional argument comes last

#Passing Different Data Types:
'''You can send any data type as an argument to a function (string, number, list, dictionary, etc.).'''

def fruit(fruits):
    for i in fruits:
        print(i)

fruits = ['apple','banana','orange']
fruit(fruits)
fruit([fruits[0]])

#Positional-Only Arguments:
'''You can specify that a function can have ONLY positional arguments.
To specify positional-only arguments, add , / after the arguments'''

def function(name,/):
    print(f'Hello {name}')
function('mk')
'''function(name = 'mk')''' #it gives error

#Keyword-Only Arguments:
'''To specify that a function can have only keyword arguments, add *, before the arguments.'''

def cities(*,city):
    print(f'{city}')

cities(city='New York')
'''cities('new york')''' #it gives error


#-----------------------------------------------------------------------------------------------------------------------

#Python *args and **kwargs:
'''By default, a function must be called with the correct number of arguments.
However, sometimes you may not know how many arguments that will be passed into your function.
*args and **kwargs allow functions to accept a unknown number of arguments.'''

#Arbitrary Arguments - *args:
'''If you do not know how many arguments will be passed into your function, add a * before the parameter name.
This way, the function will receive a tuple of arguments and can access the items accordingly:'''
'''The *args parameter allows a function to accept any number of positional arguments.
Inside the function, args becomes a tuple containing all the passed arguments:'''

def names(*names):
    print(f'type(names) = {type(names)}')
    print(f'first name = {names[0]}')
    print(f'last name = {names[-1]}')
    print(f'all names = {names}')

names('john', 'Doe', 'edwin')

def kids(*name):
    print(f'type(names) = {type(names)}')
    print(f'first kid = {name[0]}')
    print(f'second kid = {name[1]}')
    print(f'all names = {name}')

kids('mk', 'sk', 'rk')

def guest(*guests, greeting='hello'):
    for guest in guests:
        print(greeting, guest)

guest('john', 'Doe', 'edwin')

#Arbitrary Keyword Arguments - **kwargs:
'''If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
This way, the function will receive a dictionary of arguments and can access the items accordingly:'''

def introduction(**kwargs):
    print(f'type(kwargs) = {type(kwargs)}')
    print(f'name = {kwargs['name']}')
    print(f'age = {kwargs['age']}')
    print(f'city = {kwargs['city']}')

introduction(name='John', age=30, city='New York')

def intro(**agrs):
    for key, value in agrs.items():
        print(f'{key} = {value}')
intro(name='John', age=30, city='New York')

#--------------------------------------------------------------------------------------------------------------------------

#Python Scope: A variable is only available from inside the region it is created. This is called scope.

#Local Scope:
'''A variable created inside a function belongs to the local scope of that function, and can only be used inside that function'''

def myfunc():
  x = 300
  print(x)

myfunc()

'''The local variable can be accessed from a function within the function:'''
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#Global Scope
'''A variable created in the main body of the Python code is a global variable and belongs to the global scope.'''
'''A variable created outside of a function is global and can be used by anyone:'''

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

'''If you use the global keyword, the variable belongs to the global scope:'''
def myfunc():
  global x
  x = 300

myfunc()

print(x)

#Nonlocal Keyword:
'''The nonlocal keyword is used to work with variables inside nested functions.
The nonlocal keyword makes the variable belong to the outer function.'''
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

#-----------------------------------------------------------------------------------------------------------------------

#Python Lambda:
'''A lambda function is a small anonymous function
A lambda function can take any number of arguments, but can only have one expression.'''

'''lambda arguments : expression'''

x = lambda a : a + 10
print(x(5))

'''Lambda functions can take any number of arguments:'''

y = lambda a,b : a*b
print(y(1,2))

'''The power of lambda is better shown when you use them as an anonymous function inside another function.'''
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#Using Lambda with map():
'''The map() function applies a function to every item in an iterable:'''
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
