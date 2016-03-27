from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()

#print "The input file is %d bytes line" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

#out_file = open(to_file, 'w')
#out_file.write(indata)

# Perform the copy step with one line of code.
open(to_file, 'w').write(open(from_file).read())

#print "Alright, all done."

#out_file.close()  # Parenthesis are req'd on write events
				   # https://pythonconquerstheuniverse.wordpress.com/2008/06/04/gotcha-%E2%80%94-forgetting-parentheses/
#in_file.close

