# Create and write to the file
with open("learning_python.txt", "w") as file:
    file.write("In Python you can use variables to store data.\n")
    file.write("In Python you can create functions to organize your code.\n")
    file.write("In Python you can work with a variety of data types like lists, dictionaries, and sets.\n")
    file.write("In Python you can use loops to perform repetitive tasks efficiently.\n")


# Read the file in three different ways and print the contents
filename = "learning_python.txt"

# Reading the entire file at once
print("Reading the entire file:")
with open(filename) as file:
    content = file.read()
    print(content)

# Looping over the file object line by line
print("\nReading line by line:")
with open(filename) as file:
    for line in file:
        print(line.strip())

# Reading the file and working with lines stored in a list
print("\nReading into a list and printing:")
with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())
