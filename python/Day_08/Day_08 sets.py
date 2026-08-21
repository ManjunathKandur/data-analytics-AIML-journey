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

#SUBSET AND SUPER SETS:
#Subset → Smaller set fits inside a bigger set.
#Superset → Bigger set contains the smaller set.

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

print(set_a.issubset(set_b)) #set_a <= set_b/ set_a inside set_b

print(set_b.issuperset(set_a)) #set_b >= set_a / set_b contain set_a