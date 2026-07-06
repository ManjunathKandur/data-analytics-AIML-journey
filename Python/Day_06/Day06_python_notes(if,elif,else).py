#IF/ELSE/ELIF : The if statement evaluates a condition (an expression that results in True or False). If the condition is true, t
# he code block inside the if statement is executed. If the condition is false, the code block is skipped.
a = 33
b = 2988
if a>b:
    print(f'its True') #as a is not greater than b if code block skipped.

c = 10
d = 9
if c>d:
    print(f'its True') #as c is greater than d if code block runs.

#Indentation:Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
# Other programming languages often use curly-brackets for this purpose.
#If statement, without indentation (will raise an error)
#You can use spaces or tabs for indentation, but you must use the same amount of indentation for all statements within the same code block.

#Multiple Statements in If Block: You can have multiple statements inside an if block. All statements must be indented at the same level.
age = 20
if age>18:
    print(f'you can vote')
    print(f'you can get license')
    print(f'you can go to college') #make sure all line have same space.

#Using Variables in Conditions: Boolean variables can be used directly in if statements without comparison operators.
is_loged_in = True
if is_loged_in:
    print('you are logged in')

#ELSE:The else keyword catches anything which isn't caught by the preceding conditions.
#The else statement provides a default action when none of the previous conditions are true.
# Think of it as a "catch-all" for any scenario not covered by your if and elif statements.
#The else statement must come last. You cannot have an elif after an else.
n = 32
m = 54
if n>m:
    print(f'its true')
else:
    print(f'its false') #as n is not greater than m it skips if statement.

#The else statement acts as a fallback that executes when none of the preceding conditions are true.
# This makes it useful for error handling, validation, and providing default values.
username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

#ELIF: The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 78
b = 100
if a>b:
    print(f'a is greater than b')
elif a<b: #it should always have some condition to prove
    print(f'a is less than b')

#Multiple Elif Statements: You can have as many elif statements as you need.
# Python will check each condition in order and execute the first one that is true.
#Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.

Grade = 80
if Grade>80:
    print(f'A')
elif Grade>60:
    print(f'B')
elif Grade>40:
    print(f'C')
elif Grade>10:
    print(f'D')
else:
    print(f'F')

#LOGICAL OPERATORS WITH IF/ELIF/ELSE:
a =200
b = 40
c = 400
if a>b and c>b: #AND operator
    print(f'all conditions are true')
else:
    print(f'one of the condition or all conditions are false')

if a>b or b>c: #OR operators
    print(f'one of the condition is true')
else:
    print(f'all condition are false')

if not a>b: # NOT operator
    print(f'condition is true')
else:
    print(f'NOT operator working')

#Nested If:
#Each level of nesting creates a deeper level of decision-making. The code evaluates from the outermost condition inward.
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")


score = 78
attendance = 74
submitted = False
if score >= 80:
    if attendance >= 75:
        if submitted:
            print(f'Passed with good score {score}')
        else:
            print(f'Passed with good score but missing assignment')
    else:
        print(f'Passed but attendance is not {attendance}')
else:
    print(f'you failed')

#Pass Statement:if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error
a = 78
b = 100
if a>b:
    pass

