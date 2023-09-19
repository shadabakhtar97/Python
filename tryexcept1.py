
### Example 4: Using `try`...`except` for Robust Input Handling


while True:
    try:
        age = int(input("Enter your age: "))
        break  # Exit the loop if valid input is provided
    except ValueError:
        print("Invalid input. Please enter a valid age as a number.")

print("Your age is:", age)