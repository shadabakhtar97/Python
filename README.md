# python
Core and Full Stack Python Repository


### ****************************************************************************************************************************
### 				        	****** Python-Session-12.1(Hands-on): Understanding Python Exceptions ****** 
###  **************************************************************************************************************************** 
Let's dive into some hands-on examples of Python exceptions to illustrate how they work and how to
 handle them.

### Example 1: Handling a `ZeroDivisionError`

try:
    num1 = int(input("Enter a numerator: "))
    num2 = int(input("Enter a denominator: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
else:
    print("Result:", result)


In this example:
- We take user input for a numerator and denominator.
- We use a `try` block to attempt the division.
- If a `ZeroDivisionError` occurs (division by zero), we catch it and print an error message.
- If a `ValueError` occurs (invalid input that cannot be converted to an integer), we catch it and print a different error message.
- If no exceptions are raised, we print the result.

Issue:
-------
NameError: name 'file' is not defined. Did you mean: 'filter'?

Solution:
----------
with open('filename.txt', 'r') as file:
    # Your code to work with the file goes here

### Example 2: Using `finally` to Ensure Resource Closure


try:
    file = open("example.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File contents:", data)
finally:
    file.close()


In this example:
- We attempt to open a file named "example.txt" for reading.
- If a `FileNotFoundError` occurs (the file doesn't exist), we catch it and print an error message.
- If the file is successfully opened, we read its contents and print them.
- Regardless of whether an exception occurs or not, we use the `finally` block to ensure that the 
  file is closed.

### Example 3: Creating and Raising Custom Exceptions


class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom exception.")
except CustomError as e:
    print("Custom error:", e)


In this example:
- We define a custom exception class called `CustomError` by inheriting from the base `Exception` class.
- We raise an instance of our custom exception with a custom error message using the `raise` statement.
- We catch the `CustomError` exception and print the error message.

### Example 4: Using `try`...`except` for Robust Input Handling


while True:
    try:
        age = int(input("Enter your age: "))
        break  # Exit the loop if valid input is provided
    except ValueError:
        print("Invalid input. Please enter a valid age as a number.")

print("Your age is:", age)


In this example:
- We repeatedly ask the user for their age until they provide valid input (an integer).
- We use a `try`...`except` block to catch `ValueError` exceptions raised if the input cannot be converted to an integer.
- Once valid input is provided, we exit the loop and print the age.

These examples demonstrate how to handle different types of exceptions and ensure proper resource management in Python programs. Understanding and using exceptions effectively can make your code more robust and user-friendly.
