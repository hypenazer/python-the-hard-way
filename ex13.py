from sys import argv

# Takes the argument values passed in the command line and assigns to variables
# script < the filename of the script that was run in the command line
# first < the first argument (as a string)
# second < the second argument (as a string)
# third < the third argument (as a string)
script, first, second, third = argv



print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


# use int(second) to convert second to a number

# using raw_input() and argv methods in a script
x = raw_input('? ')