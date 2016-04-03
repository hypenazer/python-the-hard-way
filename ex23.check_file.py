# Script Name	: check_file.py
# Author		: Craig Richards
# Created		: 20 May 2013 
# Last Modified	: 
# Version		: 1.0

# Modifications	: 

# Description	: Check a file exists and that we can read the file

import sys		# Import the Modules
import os		# Import the Modules

# Readfile Functions which open the file that is passed to the script

def readfile(filename):
	# Open & read the file
	line = open(filename, 'r').read()
	
	# Print the file
	print line

def main():
  # Looks to see if 2 arguments were passed in the command line
  if len(sys.argv) == 2:		# Check the arguments passed to the script
	# Sets the filename variable to the second argument (arguments must be passed as a list)
    filename = sys.argv[1]		# The filename is the first argument
    # Check if the file exists ???
    if not os.path.isfile(filename):	# Check the File exists
      # Print "- filename does not exist."
      print '[-] ' + filename + ' does not exist.'
      # Exit the program
      exit(0)
    # Check if file can be accessed ???
    if not os.access(filename, os.R_OK):	# Check you can read the file
      print '[-] ' + filename + ' access denied'
      exit(0)

  # We did not receive 2 arguments in the command line
  else:
  	# Print script usage instructions 'usage: scriptname filename'
    print '[-] Usage: ' + str(sys.argv[0]) + ' <filename>' # Print usage if not all parameters passed/Checked
    exit(0)

  # We received 2 arguments, and file exists & we can access the file 
  print '[+] Reading from : ' + filename	# Display Message and read the file contents
  
  # Print the file contents ???
  readfile(filename)


# If this script is not being called by another script, run the main() function
if __name__ == '__main__':
  main()


# Need to research the following:
# os.path.isfile()
# os.access()