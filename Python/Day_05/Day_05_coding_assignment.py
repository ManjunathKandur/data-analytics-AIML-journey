#Create a dictionary of a student.
student = {
    'name' : 'mk',
    'age' : 28,
    'course' : 'Python',
}

#Take name and age as input and store them in a dictionary.
name = input("Enter your name: ")
age = int(input("Enter your age: "))

user = {
    'name' : name,
    'age' : age,
}

#Print all keys in a dictionary.
student = {
    'name' : 'mk',
    'age' : 28,
    'course' : 'Python',
}
print(student.keys())

#Print all values of a dictionary.
student = {
    'name' : 'mk',
    'age' : 28,
    'course' : 'Python',
}
print(student.values())

#Print both key and value.
student = {
    'name' : 'mk',
    'age' : 28,
    'course' : 'Python',
}
print(student)
print(student.items())

#Update a dictionary value.
student = {
    'name' : 'mk',
    'age' : 28,
    'course' : 'Python',
}

student['age'] = 29
print(student)
student.update({'age' : 30})
print(student)

#Add a new key-value pair.
student = {
    'name' : 'mk',
    'age' : 28,
    'course' : 'Python',
}

student['city'] = 'Chicago'
print(student)
student.update({'city' : 'BLG'})
print(student)

#Delete a key from dictionary.
student.pop('age')
print(student)

#Count frequency of each character in a string using dictionary.
x = "apple"

count = 0

for i in x:
    count += 1
    print({i: count})

#or

x = "apple"

count = {}

for i in x:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)

#Count frequency of each word.
x = "Python is easy Python is fun"
y = x.split()

z = {}

for i in y:
    if i in z:
        z[i] += 1
    else:
        z[i] = 1

print(z)

#Find the student with highest marks.
marks = {
    "John": 80,
    "Sam": 95,
    "David": 90
}

highest_mark = 0
highest_student = ""

for student, mark in marks.items():
    if mark > highest_mark:
        highest_mark = mark
        highest_student = student

print(highest_student, highest_mark)

#Merge two dictionaries.
d1={"a":1,"b":2}
d2={"c":3,"d":4}

d1.update(d2)
print(d1)

#Check whether a key exists
marks = {
    "John": 80,
    "Sam": 95,
    "David": 90
}
print('John' in marks)

#Sum all values of a dictionary.
x = {
"a":10,
"b":20,
"c":30
}

total = 0

for i in x.values():
    total += i

print(total)

#Create a dictionary from two lists.
keys = ["a", "b", "c"]
values = [10, 20, 30]

result = {}

for k, v in zip(keys, values):
    result[k] = v

print(result)