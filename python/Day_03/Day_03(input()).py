#INPUT(): input() is a built-in Python function that takes input from the keyboard/user.
#Python stops executing when it comes to the input() function, and continues when the user has given some input.
name = input("Enter your name: ")

#You can add as many inputs as you want, Python will stop executing at each of them, waiting for user input:
age = input("Enter your age: ")
city = input("Enter your city: ")
profession = input("Enter your profession: ")

#The input from the user is treated as a string. Even if, in the example above, you can input a number, the Python interpreter will still treat it as a string.
print(type(age)) #output is str

#To perform calculations, convert it.
age = int(input("Enter your age: ")) #output will be in int
percentage = float(input("Enter your percentage: ")) #output will be float
