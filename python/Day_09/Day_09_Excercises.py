#Practice Project 1 — Student Database
students = {}

students['s101']={
    'name':'mk',
    'age':28,
    'gender':'m'
}

students['s102']={
    'name':'kd',
    'age':29,
    'gender':'m'
}

students['s103']={
    'name':'ks',
    'age':28,
    'gender':'f'
}

students['s104']={
    'name':'gk',
    'age':29,
    'gender':'f'
}

print(students)

for roll, details in students.items():
    print(f"Roll: {roll}")
    for key, value in details.items():
        print(key, ":", value)
    print()

#Practice Project 2 — Product Inventory
inventory = {
    "Laptop": 15,
    "Mouse": 40,
    "Keyboard": 25
}

inventory['Laptop'] = 67
print(inventory)

inventory['charger'] = 99
print(inventory)

inventory.popitem() #last entered item
print(inventory)

print(inventory.keys())
print(inventory.values())

#Practice Project 3 — Employee Records
employees = {
    1:{
        "name":"Amit",
        "department":"HR",
        "salary":45000
    },
    2:{
        "name":"Sara",
        "department":"IT",
        "salary":70000
    }
}

#Practice Project 3 — Employee Records
employees = {
    1:{
        "name":"Amit",
        "department":"HR",
        "salary":45000
    },
    2:{
        "name":"Sara",
        "department":"IT",
        "salary":70000
    }
}

highest_salary = 0
person = ''

for num,info in employees.items():
    if info['salary'] > highest_salary:
        highest_salary = info['salary']
        person = info['name']
print(person)
print(highest_salary)

#Create a dictionary of 5 fruits and their prices.
fruits = {}

fruits[1] = {'name':'apple', 'price':100}
fruits[2] = {'name':'banana', 'price':200}
fruits[3] = {'name':'apricot', 'price':300}
fruits[4] = {'name':'papaya', 'price':400}
fruits[5] = {'name':'grapes', 'price':500}

for num,info in fruits.items():
    print(f'num :{num}')
    for key,value in info.items():
        print(f'{key}:{value}')
    print()

#Print all keys in a dictionary.
fruits = {}

fruits[1] = {'name':'apple', 'price':100}
fruits[2] = {'name':'banana', 'price':200}
fruits[3] = {'name':'apricot', 'price':300}
fruits[4] = {'name':'papaya', 'price':400}
fruits[5] = {'name':'grapes', 'price':500}

for num,info in fruits.items():
    for key in info.keys():
        print(key)
    print()

#Print all values in a dictionary.
fruits = {}

fruits[1] = {'name':'apple', 'price':100}
fruits[2] = {'name':'banana', 'price':200}
fruits[3] = {'name':'apricot', 'price':300}
fruits[4] = {'name':'papaya', 'price':400}
fruits[5] = {'name':'grapes', 'price':500}

for num,info in fruits.items():
    for value in info.values():
        print(value)
    print()

#Add a new key-value pair.
fruits[6] = {'name':'peach', 'price':600}

for num , info in fruits.items():
    print(f'num : {num}')
    for name, value in info.items():
        print(f'{name} : {value}')
    print()

#Update an existing value.
fruits[1]['price']=50

for num , info in fruits.items():
    print(f'num : {num}')
    for name, value in info.items():
        print(f'{name} : {value}')
    print()

#Count frequency of each character in a string.
name = "shekar krishna"

dict1 = {}

for i in name:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

print(dict1)

#Count frequency of each number in a list.
l1 = [1,2,3,5,6,7,5,4,3,5,7,5,8,9]

dict2 = {}

for i in l1:
    if i in dict2:
        dict2[i] = dict2[i] + 1
    else:
        dict2[i] = 1

for i in dict2.items():
    print(i)


