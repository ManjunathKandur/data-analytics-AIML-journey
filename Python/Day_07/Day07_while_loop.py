#while loop: With the while loop we can execute a set of statements as long as a condition is true.With the while loop we can execute a set of statements as long as a condition is true.
i = 1 #The while loop requires relevant variables to be ready
while i <= 5:
    print(i)
    i = i + 1 #remember to increment i, or else the loop will continue forever.

#break statement:
i = 0
while i < 10:
    print(i)
    if i == 7:
        break #break comes after print so it stops at 7
    i = i + 1

i = 1

while i <= 10:
    if i == 5:
        break
    print(i) #break loop before 5 as prints later break statement
    i = i + 1

#continue Statement:

a = 1
while a <= 10:
    if a == 3:
        continue
    print(a)
    a = a + 1

#Print numbers from 1 to 20.
a = 1
while a <= 20:
    print(a)
    a = a + 1

#Print even numbers from 2 to 20.
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i = i + 1

#Print odd numbers from 1 to 19.
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i = i + 1

#Use if conditions inside while
i = 1
while i <=5:
    print(i)
    i = i + 1
else:
    print("I'm done")