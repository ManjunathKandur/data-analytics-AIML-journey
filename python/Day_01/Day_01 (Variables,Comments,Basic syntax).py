#Python Syntax: python syntax can be executed by directly writing a Command Line
print("hey python!")

#-----------------------------------------------------------------------------------------------------------------------

#Print Without a New Line:If you want to print multiple words on the same line, you can use the end parameter.
print('hey',end=' ') #end will add next line to first line
print('python')

#----------------------------------------------------------------------------------------------------------------------

#Multiline Comments:Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it
""" 
This is a comment
written in
more than just one line
and python will ignore it as its not assigned to any variable 
"""

#-----------------------------------------------------------------------------------------------------------------------

#Python Variables : variables are containers for storing values. syntax: variable = value

a = 5 #varibale = value
print(a)
#Variables do not need to be declared with any particular type, and can even change type after they have been set.

a = 5 # a is int
a = 'mk' # a is string now (variables will be updated when you assign different value to same variable)
print(a)

#CASTING : If you want to specify the data type of a variable, this can be done with casting.
a = str(3) # a will be '3'
b = float(6) # b will be 6.0
c = int(7) # c will be 7
print(a,b,c)
#IMP: cannot covert string into integer eg a = int('hi')
#if you conver any data type to boolean if anything present in variable it gives out put as True , if variable is empty it gives False
t = bool(2)
r = bool() #if its empty or 0 it will give False
print(t,r)
#if you convert boolean to int if its True the output is 1 or if it's False the output will be 0
e = int(True)
f = int(False)
print(e,f)

#GET THE TYPE : You can get the data type of a variable with the type() function.
a = 10
b = 3.0
c = 'hi'
d = True
print(type(a)),print(type(b)),print(type(c)),print(type(d))

#VARIABLE NAMES: A variable name must start with a letter or the underscore character
                #A variable name cannot start with a number
                #A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
                #Variable names are case-sensitive (age, Age and AGE are three different variables)
#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
#2myvar = "John"
#my-var = "John"
#my var = "John

#Multi Words Variable Names:
myVariableName = "John" #Camel style : Each word, except the first, starts with a capital letter
MyVariableName = "John" #Pascal style : ach word starts with a capital letter
My_Variable_name = "John" #Snake style : ach word starts with a capital letter

#Python Variables - Assign Multiple Values
#Many Values to Multiple Variables : Make sure the number of variables matches the number of values, or else you will get an error.
x,y,z = 1,2,3
print(x,y,z)

#One Value to Multiple Variables:
x=y=z=3
print(x,y,z)

#Unpack a Collection:If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ['apple','orange','strawberry']
a,b,c = fruits
print(a,b,c)

#Output Variables:
#In the print() function, you output multiple variables, separated by a comma:
print(a,b,c)
#You can also use the + operator to output multiple types of variables:
print(a+b+c) #but there won't be any space btw words
#In the print() function, when you try to combine a string and integer with the + operator, Python will give you an error:
#eg print(5+'hi')
#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
print(5,'hi')


#GLOBAL VARIABLES:
#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic" #local variable works inside function
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
           #To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #tw0 same types can be print by using "+" sign

#Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
