#Build a Student Record Viewer.
students = [
    ('mk',18,97),
    ('sk',18,99),
    ('kd',18,98),
    ('ms',19,96),
    ('nr',20,96)
]

for name,age,marks in students: #Print all students using unpacking
    print(name,age,marks)

#Find the highest marks
higest_marks = (0)

for name,age,marks in students:
    if marks > higest_marks:
        higest_marks = marks
print(higest_marks)

#Print topper's name
students = [
    ('mk', 18, 97),
    ('sk', 18, 99),
    ('kd', 18, 98),
    ('ms', 19, 96),
    ('nr', 20, 96)
]

highest_marks = 0
topper = ()

for name, age, marks in students:
    if marks > highest_marks:
        highest_marks = marks
        topper = (name)

print("Topper:", topper)

#Create and Access a Tuple
user =('mk',19,'blg')
name,age,city=user
print('Name:', name)
print('Age:', age)
print('City:', city)

#Tuple Length
numbers = (5, 10, 15, 20, 25, 30, 35, 40)
print(len(numbers))

#Count Occurrences
data = (1, 2, 3, 2, 4, 2, 5)

user = int(input('enter a number: '))
count = 0

for i in data:
    if i == user:
        count += 1
print(count)

#Swap Two Variables
a=10
b=25

a,b = b,a
print(a,b)

#Highest Marks
students = (
    ("Rahul", 85),
    ("Anita", 92),
    ("Kiran", 78),
    ("Sara", 95)
)

top_marks = (0)

for name,marks in students:
    if marks > top_marks:
        top_marks = marks
print(top_marks)