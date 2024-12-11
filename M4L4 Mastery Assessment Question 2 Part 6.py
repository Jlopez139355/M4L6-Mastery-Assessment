# Create and write to the file
with open("learning_python.txt", "w") as file:
    file.write("In Python you can use variables to store data.\n")
    file.write("In Python you can create functions to organize your code.\n")
    file.write("In Python you can work with a variety of data types like lists, dictionaries, and sets.\n")
    file.write("In Python you can use loops to perform repetitive tasks efficiently.\n")


# Define the filename
filename = "learning_python.txt"

# Read the file, replace "Python" with "C", and print each modified line
with open(filename) as file:
    for line in file:
        modified_line = line.replace("Python", "C")
        print(modified_line.strip())
