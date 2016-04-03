# This file will contain notes for exercise 22.
# 

ex1:
print "text"


ex2:
# comment


ex3:
# integers vs decimal with division
# + plus -- addition
# - minus -- subtraction
# / slash -- division	
# % percent -- mod
# < less-than
# > greater-than
# <= less-than-equal
# >= greater-than-equal	


ex4:
# variables
string_variable = "text"
print "text here ", string_variable, " trailing text."


ex5:
# Formatting variables in line with text
print "this is my %s text" % string_variable
print "my age is %d" % int_dec_variable
print "my age is %04d" % int_dec_variable # Pads with 4 zeros
print "my age is %4d" % int_dec_variable # Pads with 4 spaces
print "%06.2f inches tall." % float_variable # Print 6 places with 2 after decimal and pad with 0s
print "%r" % any_variable # Print any type of variable
# Full list of conversions are here:
# https://docs.python.org/2/library/stdtypes.html#string-formatting


ex6:
# Binary variables
binary_variable = False


ex7:
# String concatenation
print var1 + var2 + var3 , var4
# + performs concatenation
# , concatenates and adds a space character

# Python style is to limit lines to 80 characters


ex8:
# A string variable can be used to format the output
formatter = "%r, %r, %r, %r"
print formatter % (1, 2, 3, 4)


ex9:
# Three double-quotes are treated as literals
"""This is my literal
and it accepts new lines"""

# \n is treated as new line character


ex10:
# Python escape characters:
# \\ Backslash (\)
# \' Single-quote (')
# \" Double-quote (")
# \a ASCII bell (BEL)
# \b ASCII backspace (BS)
# \f ASCII formfeed (FF)
# \n ASCII linefeed (LF)
# \N{name} Character named name in the Unicode database
# \r Carriage return(CR)   <-- I wasn't able to get this to work on osx
# \t Horizontal Tab (TAB)
# \uxxx Character with 16-bit hex value xxxx
# \Uxxxxxxxx Character with 32-bit hex value xxxxxxxx
# \v ASCII vertical tab (VT)
# \ooo character with octal value ooo
# \xhh character with hex value


ex11:
# Prompt users for input with
raw_input()
# Raw input must be converted to numbers
int(raw_input())


ex12:
# pydoc [function] displays python documentation about the function
pydoc raw_input


ex13:
# Import modules using the following
from sys import argv 

# argv is used to pass command line arguments
script, flag1, flag2 = argv  # flag1 = command line argument1, etc. 

# Modify the raw_input prompt
raw_input('? ')


ex14:
# Modify the raw_input prompt with a string
sting_var = "Prompt: "
user_input = raw_input(string_var)


