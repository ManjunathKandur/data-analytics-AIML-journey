#TUPLS: ordered,indexed,unchangeable,allow duplicates
#Tuples are written with round brackets.()
y = ("mk",1,True)
print(y)

#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Python - Access Tuple Items
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
print(y[0])

#Negative Indexing:-1 refers to the last item, -2 refers to the second last item etc.
print(y[-1])

#Python - Update Tuples
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
y = ("mk",1,True)
x=list(y)
x[0] = "sk"
y = tuple(x)
print(y)

#Add Items
y = ("mk",1,True)
x = list(y)
x.append("sk")
x.extend("apple",) #it adds each letter separetly at end so use append/insert
x.insert(0,"mk")
y = tuple(x)
print(y)

#Python - Unpack Tuples
#we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ['apple','orange','grape']
x,y,z = fruits
print(x)
print(y)
print(z)

#Using Asterisk*:
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Python - Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#or
tuple1+=tuple2
print(tuple1)
print(tuple1.count(2)) #counts the items/value
print(tuple1.index(2)) #specify the index of item/value
