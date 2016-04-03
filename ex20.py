# Import the command line argument module
from sys import argv

# Store the file name from the command line arguments as input_file
script, input_file = argv

# Create a function that prints the content of file "f"
def print_all(f):
	print f.read()

# Create a function that moves to the starting position of file "f"
def rewind(f):
	f.seek(0)

# Create a function that prints the next line of file "f"
def print_a_line(line_count, f):
	print line_count, f.readline(), # Trailing comma strips \n from line

# Open the file passed in the command line
current_file = open(input_file)

print "First let's print the whole file:\n"

# Print the content of the file passed in the command line
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# Move to the starting position of the file
rewind(current_file)

print "Let's print three lines:"

# Print the next line of the file
current_line = 1
print_a_line(current_line, current_file)  # current_line = 1

# Print the next line of the file 
current_line += 1
print_a_line(current_line, current_file)  # current_line = 2

# Print the next line of the file
current_line += 1
print_a_line(current_line, current_file)  # current_line = 3