# 🐍 Day 12 — Python Functions

> 📅 **Date:** August 24, 2026
> 🎯 **Topic:** Functions
> 📚 **Learning Track:** Data Analytics with AI/ML

---

## 🎯 Learning Objectives

Today I learned how to create and use Python functions to write reusable and organized code.

### Topics Covered

* 🔹 Function creation using `def`
* 🔹 Parameters
* 🔹 Arguments
* 🔹 `return` statement
* 🔹 Default arguments
* 🔹 Keyword arguments
* 🔹 Local and global scope
* 🔹 Lambda functions
* 🔹 Reusable functions
* 🔹 Functions with multiple parameters

---

## 📖 Concepts Learned

### 1️⃣ Creating a Function

```python
def greet():
    print("Hello!")

greet()
```

---

### 2️⃣ Parameters and Arguments

```python
def greet(name):
    print("Hello", name)

greet("Manjunath")
```

* `name` → Parameter
* `"Manjunath"` → Argument

---

### 3️⃣ Return Statement

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

### `print()` vs `return`

* `print()` displays a value.
* `return` sends a value back from the function so it can be reused.

---

### 4️⃣ Default Arguments

```python
def greet(name="User"):
    print("Hello", name)

greet()
greet("Manjunath")
```

---

### 5️⃣ Keyword Arguments

```python
def student(name, age, marks):
    print(name, age, marks)

student(
    name="Manjunath",
    age=25,
    marks=85
)
```

---

### 6️⃣ Scope

#### Local Variable

```python
def test():
    x = 10
    print(x)
```

`x` is available inside the function.

#### Global Variable

```python
x = 100

def test():
    print(x)

test()
```

`x` is defined outside the function and can be accessed inside it.

---

### 7️⃣ Lambda Function

A lambda function is a small anonymous function.

```python
square = lambda x: x ** 2

print(square(5))
```

Output:

```text
25
```

Another example:

```python
add = lambda a, b: a + b

print(add(10, 20))
```

---

# 🧮 Practice

## Calculator Functions

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
```

---

## 🏋️ BMI Calculator

```python
def calculate_bmi(weight, height):
    return weight / (height ** 2)

bmi = calculate_bmi(70, 1.75)

print("BMI:", bmi)
```

---

## 🔢 Math Utilities

```python
def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def is_even(n):
    return n % 2 == 0

def maximum(a, b):
    return max(a, b)

def minimum(a, b):
    return min(a, b)
```

---

# 📝 Practice Exercises

### Beginner

* [x] Create a greeting function
* [x] Create an addition function
* [x] Create a subtraction function
* [x] Create a multiplication function
* [x] Create a division function
* [x] Create a square function
* [x] Create a cube function
* [x] Check whether a number is even or odd

### Intermediate

* [x] Create a calculator using functions
* [x] Create a BMI calculator
* [x] Create math utility functions
* [x] Practice default arguments
* [x] Practice keyword arguments
* [x] Practice lambda functions
* [x] Practice local and global scope

---

# 🚀 Day 12 Assignment

## Student Result Calculator

Create a program using functions that:

1. Accepts the student's name
2. Accepts marks for 5 subjects
3. Calculates total marks
4. Calculates percentage
5. Determines the grade
6. Displays a formatted result

### Suggested Functions

```python
def get_total():
    pass

def calculate_percentage():
    pass

def calculate_grade():
    pass

def display_result():
    pass
```

### Expected Output

```text
================================
       STUDENT RESULT
================================

Student Name: Manjunath

Subject 1: 85
Subject 2: 78
Subject 3: 92
Subject 4: 88
Subject 5: 80

Total      : 423
Percentage : 84.60%
Grade      : A

================================
```

---

# 🧠 Key Takeaways

> 💡 Functions help us write **reusable, organized, and maintainable code**.

### Important Syntax

```python
def function_name(parameters):
    # code
    return result
```

### Remember

| Concept          | Meaning                                |
| ---------------- | -------------------------------------- |
| `def`            | Creates a function                     |
| Parameter        | Variable defined in a function         |
| Argument         | Actual value passed to a function      |
| `return`         | Sends a result back                    |
| Default argument | Parameter with a predefined value      |
| Keyword argument | Argument passed using parameter name   |
| Local scope      | Variable available inside its function |
| Global scope     | Variable defined outside functions     |
| `lambda`         | Small anonymous function               |

---

# 🔄 Active Recall

Before moving to the next day, I should be able to answer:

* ❓ What is a function?
* ❓ Why are functions useful?
* ❓ What is the difference between a parameter and an argument?
* ❓ What is the difference between `print()` and `return`?
* ❓ What are default arguments?
* ❓ What are keyword arguments?
* ❓ What is variable scope?
* ❓ What is a lambda function?
* ❓ How do I create a calculator using functions?

---

# 💻 GitHub Progress

### Commit Message

```text
Day 12: Learned Python Functions
```

### Skills Added

```text
Python
├── Functions
├── Parameters
├── Arguments
├── Return values
├── Default arguments
├── Keyword arguments
├── Scope
└── Lambda functions
```

---

## 📈 Learning Progress

**Day 12 / Python Fundamentals**

```text
████████████████████░░░░░░░░  Functions
```

> 🚀 **Next:** Continue building Python fundamentals and strengthen problem-solving through functions and real-world mini projects.

