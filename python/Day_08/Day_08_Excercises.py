#Create a set of 5 colors and print it.
colours = {'red', 'green', 'blue','yellow','cyan'}
print(colours)

#Add a new color to a set.
colours.add('magenta')
print(colours)

#Remove a color from a set.
colours.remove('magenta')
print(colours)
colours.discard('yellow')
print(colours)
colours.pop() #removes random item
print(colours)

#Convert a list with duplicates into a set.
list1 = [1,1,3,5,6,3,4,7,6]
set1 = set(list1)
print(set1)

#Count unique numbers in a list.
list1 = [1,1,3,5,6,3,4,7,6]
set2 = set(list1)
print(len(set2))

#Find common students between two classes.
class_1 = {'mk','kd','rk'}
class_2 = {'mk','sk','rk'}

common_set = class_1 & class_2
common_set2 = class_1.intersection(class_2)
class_1.intersection_update(class_2)

print(common_set)
print(common_set2)
print(class_1)

#Find students present only in Class 1
class_1 = {'mk','kd','rk'}
class_2 = {'mk','sk','rk'}

unique_class=class_1.difference(class_2)
unique_class_1 = class_1-class_2
class_1.difference_update(class_2)

print(unique_class)
print(unique_class_1)
print(class_1)

#Find students present only in one of the two classes.
class_1 = {'mk','kd','rk'}
class_2 = {'mk','sk','rk'}

student = class_1 ^ class_2
students = class_1.symmetric_difference(class_2)
class_1.symmetric_difference_update(class_2)

print(student)
print(students)
print(class_1)

#Merge two class
class_1 = {'mk','kd','rk'}
class_2 = {'mk','sk','rk'}

all_students = class_1 | class_2
students = class_1.union(class_2)

print(students)
print(all_students)

#Check whether one set is a subset of another.
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

print(set_a.issubset(set_b)) #set_a <= set_b

print(set_b.issuperset(set_a))

