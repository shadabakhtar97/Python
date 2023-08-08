# Python Using pop() Function

# Python 3 code to demonstrate
# working of pop()

# initializing dictionary
test_dict = {"Nikhil": 7, "Akshat": 1, "Akash": 2}

# Printing initial dict
print("The dictionary before deletion : " + str(test_dict))

# using pop to return and remove key-value pair.
pop_ele = test_dict.pop('Akash')

# Printing the value associated to popped key
print("Value associated to popped key is : " + str(pop_ele))

# Printing dictionary after deletion
print("Dictionary after deletion is : " + str(test_dict))
