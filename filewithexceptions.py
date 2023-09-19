with open('example.txt', 'r') as file:
    # Your code to work with the file goes here
 try:
    file = open("example.txt", "r")
    data = file.read()
 except FileNotFoundError:
    print("File not found.")
 else:
    print("File contents:", data)
 # finally:
 #   file.close()