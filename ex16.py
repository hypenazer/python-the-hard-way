# Python functions to remember:
# close -- Closes the file
# read - Reads the contents of a file
# readline - Reads just one line of a text file
# truncate - Empties the file
# write('stuff') - Writes 'stuff' to the file

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# Open the file for write purposes
target = open(filename, 'w')
# 'r'      -- reading only
# 'r+'     -- reading and writing (file must already exist)
# 'w'/'w+' -- truncate the existing file -or- create if it doesn't exist
# 'a'/'a+  -- open the file -or- create if it doesn't exist;
#             writes are appends (unless the fseek function is used)

print "Truncating the file.  Goodbye!"
target.truncate()  # this is not needed if file is opened with w/w+

#print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

#print "I'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# Alternate write method:
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

#print "And finally, we close it."
target.close()