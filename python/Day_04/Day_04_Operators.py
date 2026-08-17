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


#Ternary Operator:The ternary operator allows you to assign one value if a condition is true, and another if it is false.
#The ternary operator is not an actual operator, it is a conditional expression, or a shorthand if statement.
num = 6

x = "WEEKEND!" if num > 5 else "Workday"

print(x)
