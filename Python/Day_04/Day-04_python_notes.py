#LISTS: Lists are created using square brackets.
my_list = [1,2,3,4,5,6,7,8,9]
print(my_list)
#List items are indexed, the first item has index [0], the second item has index [1] etc.
print(my_list[0])
print(my_list[1])

#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list.
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

#Since lists are indexed, lists can have items with the same value(duplicates)
list0 = [1,1,2,2,3,3]
print(list0)

#To determine how many items a list has, use the len() function:
print(len(list0))

#A list can contain different data types
list1 = [1,True,'mk',2.0]
print(list1)
print(type(list1)) #to check type use type()

#It is also possible to use the list() constructor when creating a new list.
list2 = list((1,'mk',5,True))
print(list2)

#Access Items
list3 = [1,True,'sk',False,3.0]
print(list3[0]) #1st item always 0
print(list3[1]) #2nd item is 1
print(list3[-1]) # -1 represents first value from last
print(list3[0:3]) #range of items also can be printed and item 3 is not included
print(list3[:3])
print(list3[2:])

#Change List Items
list4 = [2,5.6,'sk',True,False]
list4[1] = 8 #To change the value of a specific item, refer to the index number
print(list4)

#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
thislist = ['apple','orange','grape','banana']
thislist[0:2] = ['strawberry','guava']
print(thislist)

#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
fruits = ['apple','orange','grape']
fruits[1:2] = ['strawberry','guava']
print(fruits)

#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
fruits = ['apple','orange','grape']
fruits[0:2] = ['guava']
print(fruits)

#Add List Items:
fruits = ['apple','orange','grape']
fruits.append('guava') #it always add new item to last
print(fruits)
fruits.insert(0,'grape') #in insert we need to specify on which index u need new item
print(fruits)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #extend will join two list (and extend can be used to list and tuples too)
print(thislist)

#Remove List Items:
list6 = [1,'mk','apple',True,4.6]
list6.remove('apple') #remove specified item
print(list6)
list6.pop(0) #pop will remove specified index
print(list6)
list6.pop()  #pop without index will always remove last item
print(list6)

list7 = ['apple','orange','grape',1,2.3,True,False]
del list7[0] #del removed specified index if we use (del list7 = will delete the full list)
print(list7)
list7.clear() #its clears the list not delete it like del
print(list7)

#Loop Lists
list8 = ['apple','orange','grape',1,2.3,True,False]

for i in list8:
    print(i)

for i in range(len(list8)):
    print(list8[i])

i = 0
while i < len(list8):
    print(list8[i])
    i = i +1

fruits = ['apple', 'banana', 'cherry']
newlist = []
for x in fruits:
    if x == 'cherry':
        newlist.append(x)
print(newlist)

fruits = ['apple', 'orange','grape']
nlist = []
for x in fruits:
    if 'p' in x:
        nlist.append(x)
print(nlist)

#Sort Lists
a = [1,2,3,4,5,6,7,8,9]
a.sort() #sorts ascending order or alphabetically
print(a)
a.sort(reverse=True) #its sort in descending order r reverse alphabetically
print(a)
b = ['apple','Orange','grape']
b.reverse() #its just reverse the list
print(b)
b.sort(key = str.lower) #sort based on lower case and upper case
print(b)

#Copy Lists
e = [1,3,4,6,7]
m = e.copy() #its copy the list
print(m)
n = list(e) #list() method
print(n)
o = e[:] #slicing method
print(o)

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
print(tuple1.index(2)) #specify the index pf item/value