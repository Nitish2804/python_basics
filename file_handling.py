# # Open a file in read mode
# file = open("example.txt", "r")

# # Open a file in write mode
# file = open("example.txt", "w")

# # Open a file in append mode
# file = open("example.txt", "a")

# # Open a file in read and write mode
# file = open("example.txt", "r+")

# # Open a file in binary mode
# file = open("example.txt", "rb")
# content = file.read()
# file.close



# file = open("example.txt", "r")

# # Remember to close the file after you're done with it


# file = open("example.txt", "w")
# file.write("Hello, world!\n")
# file.write("This is a new line.\n")
# file.close()



# file = open("example.txt", "a")
# file.write("This line will be appended.\n")
# file.close()


# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)


# with open("example.txt", "rb") as file:
#     binary_data = file.read()
#     # Process binary data as needed


# with open("sample.txt", "r") as file:
#     content = file.read()
#     print(content)



# with open("sample.txt", "w") as file:
#     content = file.write
#     file.write("Acer\n")
#     file.write("This is a new line.\n")
#     print(content)

# with open("sample.txt", "w") as file:
#     content = file.write("Acer\n")  # Write content to file and capture the return value
#     file.write("This is a new line.\n")
#     print(content)  # Print the return value of the write operation

# with open("sample.txt", "a") as file:
#     content = file.write("and\n")  
#     file.write("This line will be appended.\n")
#     print(file.read())  

with open("sample.txt", "r") as file:
     content = file.read()
     print(content)