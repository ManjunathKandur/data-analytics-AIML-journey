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


#_________________________________________________________________________________________________________________________________________________________________________________________________________________________


#PYTHON DATA TYPES:
#Text Type:	str Eg: 'hi'
#Numeric Types:	int, float, complex eg:6, 7.0, 1+7j
#Sequence Types:list, tuple, range eg:[],(),range(0,6)
#Mapping Type:	dict eg:{name:'mk',age:16}
#Set Types:	set, frozenset eg:{},({})
#Boolean Type:	bool eg:True,False
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType

#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#Python input() Function: The input() function allows user input. syntax: input(prompt)
x = input("What is your name?")
print('hi',x)

#user input will always be in string so to avoid that use casting to get desired input
x = int(input("What is your age?")) #it will conver input into integer.
print(f'are you {x} years old') #f is special function which helps to write different data types in single sentence.

#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#PYTHON OPERATORS: Operators are used to perform operations on variables and values.
#Arithmetic Operators: Arithmetic operators are used with numeric values to perform common mathematical operations
w = 8
u = 10
print(w+u) #addition/sum
print(w-u) #substraction
print(w*u) #multipliation
print(w/u) #devision(it always gives float)
print(w//u) #floor division(it always give integer, down to the number)
print(w%u) #modulus (It is used to find the remainder left over after dividing one number by another.)
print(w**u) #power/exponential (syntax : base ** exponent)

#Assignment Operators: Assignment operators are used to assign values to variables.
k =8
k +=10 #k = k + 10
print(k)
k -= 8 #k = k - 8
print(k)
k *= 10 #k = k * 8
k /= 2 #k = k / 2
k //= 1 #k = k // 1
k **= 2 #k = k ** 2
print(k)

#Comparison Operators : to compare variables or values.Comparison operators return True or False based on the comparison:
d=10
e=9
print(d==e) #equals
print(d!=e) #not equal
print(d>e) #greater than
print(d<e) #smaller than
print(d >= e) #greater than or equals
print(d <= e) #smaller than or equals

#Logical Operators:Logical operators are used to combine conditional statements
#AND operator : Returns True if all conditions True
d = 8
print(d == 8 and d < 10)
print(d > 8 and d < 10)

#OR operator: Returns True if one condition/statement is true
print(d == 8 or d !=8)

#NOT operator: Reverse the result, returns False if the result is true
print(not(d == 8 and d < 10))
print(not(d > 8 and d < 10))

#Identity Operators: Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
#IS operator : The is operator returns True if both variables point to the same object
x = 'hi'
y = 'mk'
print(x is y)
x = y #is - Checks if both variables point to the same object in memory
print(x is y)

# IS NOT operator: The is not operator returns True if both variables do not point to the same object
r = ['apple','orange','strawberry']
t = ['apple','orange','strawberry']
print(r is not t) #True because r and t not pointing same object
r = t
print(r is not t) #False because r and t point at each other / same object

#Membership Operators: Membership operators are used to test if a sequence is presented in an object
#IN operator:Returns True if a sequence with the specified value is present in the object
s = 'Hello'
print('H' in s) #True because H is in Hello

#NOT IN : Returns True if a sequence with the specified value is not present in the object
print('i' not in s) #True because i is not in Hello


#Operator Precedence: Operator precedence describes the order in which operations are performed
#The precedence order is described in the table below, starting with the highest precedence and ending with lowest
#PARANTHESIS(),EXPONENTIAL**,(Unary plus, unary minus, and bitwise NOT+x,-x),(Multiplication*, division/, floor division//, modulus%),(addition+,subtraction-)
#If two operators have the same precedence, the expression is evaluated from left to right.
print(5 + 4 - 7 + 3) #Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right
print(7*8/2//2%1) #The operators *, /, //, and % all have the same precedence level. So Python evaluates them from left to right.