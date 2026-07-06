#Python Dictionaries: which is ordered*, changeable and do not allow duplicates.
#ictionaries are used to store data values in key:value pairs.
#Dictionaries are written with curly brackets, and have keys and values {}

car = {"Brand" : "Ford", #Brand = key and ford = value
       "Model" : "Mustang",
       "Year" : 1999}
print(car)

#The values in dictionary items can be of any data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#It is also possible to use the dict() constructor to make a dictionary.
dict1 = dict(name = 'mk',age = 28,city = 'blg')
print(dict1)

#--------------------------------------------------------------------------------------------------------------------------------------------

#Python - Access Dictionary Items:
#You can access the items of a dictionary by referring to its key name, inside square brackets

dict2 = {
    'name': 'MK',
    'age': 28,
    'city': 'blg'
}
print(dict2['name'])

x = dict2['name']
print(x)

#There is also a method called get() that will give you the same result:
print(dict2.get('age'))

y = dict2.get('age')
print(y)

#Get Keys: .keys() : extract only  keys
print(dict2.keys())

z = dict2.keys()
print(z)

#Get Values : .values() extract only values
print(dict2.values())

a = dict2.values()
print(a)

#Get Items : .items() extract both key and value
print(dict2.items())

b = dict2.items()
print(b)

#-------------------------------------------------------------------------------------------------------------------------------

#Python - Change Dictionary Items:
#You can change the value of a specific item by referring to its key name.
dict2 = {
    'name': 'MK',
    'age': 28,
    'city': 'blg'
}
dict2["name"] = ('sk')
print(dict2)

#Update Dictionary: .update()
dict2.update({"name":"mk"})
print(dict2)

#--------------------------------------------------------------------------------------------------------------------------

#Python - Add Dictionary Items:
#Adding an item to the dictionary is done by using a new index key and assigning a value to it
dict2 = {
    'name': 'MK',
    'age': 28,
    'city': 'blg'
}
dict2["fav color"] = "red"
print(dict2)

#Update Dictionary: .update({})
dict2 = {'name': 'MK',
    'age': 28,
    'city': 'blg'
}
dict2.update({"fav color": "red"})
print(dict2)

#--------------------------------------------------------------------------------------------------------------------------------

#Python - Remove Dictionary Items:
#There are several methods to remove items from a dictionary:
dict2.pop("fav color") #pop method: The pop() method removes the item with the specified key name
print(dict2)

dict2.popitem() #popitem() method : removes last entered items
print(dict2)

del dict2["name"] #del method : but del without specified key it will delete entier dic
print(dict2)

dict2.clear() #clear() method : its removes all items from dic
print(dict2)

#-----------------------------------------------------------------------------------------------------------------------------------

#Loop Through a Dictionary
#You can loop through a dictionary by using a for loop.
dict2 = {'name': 'MK',
    'age': 28,
    'city': 'blg'
}

for i in dict2: #its extract all keys of dic
    print(i)

for i in dict2.keys(): #it extracts all keyvalues
    print(i)

for i in dict2.values(): #it extracts all values of dic
    print(i)

for i in dict2.items(): #it extracts both values : keys
    print(i)

#---------------------------------------------------------------------------------------------------------------------------------------------

#Python - Copy Dictionaries:
#There are ways to make a copy, one way is to use the built-in Dictionary method copy().
dict2 = {'name': 'MK',
    'age': 28,
    'city': 'blg'
}

dict3 = dict2.copy()
print(dict3)

#Another way to make a copy is to use the built-in function dict()
dict4 = dict(dict2)
print(dict4)

#---------------------------------------------------------------------------------------------------------------------------------------

#Python - Nested Dictionaries
#A dictionary can contain dictionaries, this is called nested dictionaries.
fam = {'father' : {
    'name' : 'ck',
    'age' : 65
},
    'mother' : {
        'name' : 'gk',
        'age' : 52
    },
    'bother' : {
        'name' : 'sk',
        'age' : 29
    },
    'sister' : {
        'name' : 'ak',
        'age' :34
    }

}

print(fam)
print(fam['father']['name'])
print(fam['mother']['name'])

#---------------------------------------------------------------------------------------------------------------------------------------

#python SET:A set is a collection which is unordered, unchangeable*, and unindexed.
#Sets are written with curly brackets.{}

set1 = {'apple','banana'}
print(set1)

#Sets cannot have two items with the same value.
set2 = {"apple", "banana", "cherry", "apple"}
print(set2)

#The values True and 1 are considered the same value in sets, and are treated as duplicates:
set3 = {"apple", "banana", "cherry", True, 1, 2}
print(set3)

#-------------------------------------------------------------------------------------------------------------------------------

#Python - Access Set Items:
#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop,

for i in set3:
    print(i)

#ask if a specified value is present in a set, by using the in keyword.
print(2 in set3)

#Once a set is created, you cannot change its items, but you can add new items.

#-------------------------------------------------------------------------------------------------------------------------------

#Python - Add Set Items:
#To add one item to a set use the add() method.
set3 = {"apple", "banana", "cherry", True, 1, 2}
set3.add(3)
print(set3)

#To add items from another set into the current set, use the update() method.
set2.update(set3)
print(set2)

#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

#----------------------------------------------------------------------------------------------------------------------------------------

#Python - Remove Set Items:
#To remove an item in a set, use the remove(), or the discard() method.
set3.remove(3)
set3.discard(2)
print(set3)

#You can also use the pop() method to remove an item, but this method will remove a random item,
set3.pop()
print(set3)

#----------------------------------------------------------------------------------------------------------------------------------------

#Python - Loop Sets: You can loop through the set items by using a for loop:

for i in set2:
    print(i)

#----------------------------------------------------------------------------------------------------------------------------------------

#Python - Join Sets
#Union: The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set3 = set1 | set2 #same as union
print(set3)

#Intersection:The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {1, 2, 3}
set2 = {'a','b',2}
set3 = set1.intersection(set2)
print(set3)

set3 = set1 & set2 #same as intersection
print(set3)

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1.intersection_update(set2)
print(set1)

#Difference: The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {1, 2, 3}
set2 = {'a','b',2}
set3 = set1.difference(set2)
print(set3)

set3 = set1 - set2
print(set3)
set3 = set2 - set1
print(set3)

set1.difference_update(set2)
print(set1)

#Symmetric Differences:The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {1, 2, 3}
set2 = {'a','b',2}

set3 = set1.symmetric_difference(set2)
print(set3)

set3 = set1 ^ set2
print(set3)

set1.symmetric_difference_update(set2)
print(set1)

#-------------------------------------------------------------------------------------------------------------------------------------

#Python frozenset: frozenset is an immutable version of a set.
#Unlike sets, elements cannot be added or removed from a frozenset.
#Use the frozenset() constructor to create a frozenset from any iterable.
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

#------------------------------------------------------------------------------------------------------------------------------------

