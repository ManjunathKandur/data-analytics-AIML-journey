#Create a list of 5 fruits and print all elements.
from enum import unique

fruits = ['apple','orange','banana','cherry','mango']
print(fruits)

#Print the first and last element of a list.
print(fruits[0])
print(fruits[-1])

#Print every alternate element.
print(fruits[::2])

#Replace the third element with another value.
fruits[2] = 'kiwi'
print(fruits)

#Add a new element at the end
fruits.append('guva')
print(fruits)

#Insert an element at index 2.
fruits.insert(2,'papaya')
print(fruits)

#Delete the first element.
fruits.pop(0)
print(fruits)

#Count how many times a number appears.
x = [10,20,30,20,20]
count = 0

for num in x:
    if num == 20:
        count += 1

print(count)

#Find the length of a list.
print(len(x))

#Check whether a value exists in a list.
print(20 in x)
print(70 in x)

#Find the largest number in a list.
x = [10,20,30,20,20]
print(max(x))

largest = x[0]

for i in x:
    if i > largest:
        largest = i

print(largest)

#Find the smallest number.
print(min(x))
smallest = x[0]

for i in x:
    if i < smallest:
        smallest = i

print(smallest)

#Calculate the sum of all numbers.
print(sum(x))

total = 0
for i in x:
    total += i
print(total)

#Calculate the average.
total = 0

for i in x:
    total +=i

average = total/len(x)
print(average)

#Reverse a list.
fruits.reverse()
print(fruits)

#Sort a list in ascending order.
x.sort()
print(x)

#Sort a list in descending order.
x.sort(reverse = True)
print(x)
fruits.sort(reverse = False)
print(fruits)

#Remove duplicate elements from a list.
x = list(set(x))
print(x)
#or
x = [10,20,30,20,20]
unique = []

for i in x:
    if i not in unique:
        unique.append(i)
print(unique)

#Create a tuple of 5 cities.
cities = ['bangalore','mumbai','gulbarga','hyderabad','delhi']
print(cities[0]) # first city
print(cities[-1]) #last city

#middle city
cities = ['bangalore','mumbai','gulbarga','hyderabad','delhi']
city = []
for i in range(len(cities)):
    if i == len(cities)//2:
        city.append(cities[i])

print(city)

#