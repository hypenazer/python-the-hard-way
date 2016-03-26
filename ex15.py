# Load the argv module to enable command line arguments
# Command line is preferred as it can use tab-complete
from sys import argv

# Give variable names to the arguments passed through command line
script, filename = argv

# Open the name of the file passed in command line
txt = open(filename)

# Print the name of the file received in command line
print "Here's your file %r:" % filename
# Print the content of the file
print txt.read()

# Prompt the user for the name of a file to open 
print "Type the filename again:"
file_again = raw_input("> ")

# Open the file entered by the user
txt_again = open(file_again)

# Print the content of the file entered by the user
print txt_again.read()

# Close the files
txt.close()
txt_again.close()