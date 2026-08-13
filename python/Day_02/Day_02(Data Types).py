#PYTHON DATA TYPES:
#Text Type:	str Eg: 'hi'
a = 'mk'

#Numeric Types:	int, float, complex eg:6, 7.0, 1+7j
b = 6 #Integers can be positive, negative, or zero.
c = 7.0
d = 1+7j

#Sequence Types:list, tuple, range eg:[],(),range(0,6)
e = ['mk',1,6.0] #list
f = ('mk',1,7.0) #tuple
g = range(0,10) #range

#Mapping Type:	dict eg:{name:'mk',age:16}
h = {'name':'mk','age':28}

#Set Types:	set, frozenset eg:{},({})
i ={'mk',1,9.0,True}
j = ({'mk',2,9.3})

#Boolean Type:	bool eg:True,False
k = True
l = False

#Binary Types:	bytes, bytearray, memoryview
m = memoryview(bytes(5))

#None Type:	NoneType
n = None

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
print(n)

#-----------------------------------------------------------------------------------------------------------------------

#Getting the Data Type:You can get the data type of any object by using the type() function.
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))

#-----------------------------------------------------------------------------------------------------------------------

#Setting the Specific Data Type/casting:If you want to specify the data type of a variable, this can be done with casting.
a = str(3) # a will be '3'
b = float(6) # b will be 6.0
c = int(7) # c will be 7
print(a,b,c)
#IMP: cannot covert string into integer eg a = int('hi')
#if you convert any data type to boolean if anything present in variable it gives out put as True , if variable is empty it gives False
t = bool(2)
r = bool() #if its empty or 0 it will give False
print(t,r)
#if you convert boolean to int if its True the output is 1 or if it's False the output will be 0
e = int(True)
f = int(False)
print(e,f)

