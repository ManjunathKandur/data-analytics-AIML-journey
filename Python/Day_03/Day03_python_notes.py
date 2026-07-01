#STRING:Strings in python are surrounded by either single quotation marks, or double quotation marks. 'hello' is the same as "hello".
#You can use quotes inside a string, as long as they don't match the quotes surrounding the string
print('hi im "Manjunath" ')
print("Hi im 'Manjunath'")

#Multiline Strings: You can assign a multiline string to a variable by using three quotes
a = '''hi im "MK",
i stay in "BNG",
i drive car'''
print(a)

#Python - SLICING STRINGS: You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.

b = 'hello world!'
print(b[2:5]) #REMEMBER 1st LETTER IS ALWAYS 0 , and 5th POSITION(last position ) will always not include.
print(b[:3]) #slicing from start
print(b[2:]) #slice to end

#Negative Indexing : Use negative indexes to start the slice from the end of the string
print(b[-5:-2]) #during negative indexing last letter will be always -1 and -2 is excluded here

#Step slicing:string[start:end:step]
c = 'manjunath'
print(c[1:8:2]) #step means the number of jumps

#Python - MODIFYING STRINGS: Python has a set of built-in methods that you can use on strings.
print(c.upper())
print(c.lower())
print(c.title())
print(c.strip())
print(c.replace('m','n'))
print(c.count('m'))
print(c.find('m'))
print(c.split()) #split will always result into list

#Python - STRING CONCATENATION: To concatenate, or combine, two strings you can use the + operator
a = 'Hello'
b = 'World!'
c = a+b #its does not give space bte words
print(c)
d = a+' '+b # it adds space
print(d)

#Python - FORMAT - STRINGS:As we learned in the Python Variables chapter, we cannot combine strings and numbers like this
#F-Strings : To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age = 18
txt = f'Hi my name is MK and my age {age}'
print(txt)
print(f'my age is {age}')

#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals
price = 59
print(f'my price is {price:.2f}')


#Python - Escape Characters:
txt = 'It\'s alright.' #\' single quote
t = 'it is \\  alright' #\\ backlash
n = 'it\'s new \n line' #\n new line
e = 'its\tis lovely'#\t tab
f = 'its is\b  lovely' #\b back space

#Reverse String: syntax(variable[::-1])
w = 'python'
print(w[::-1]) #it writes string reverse


