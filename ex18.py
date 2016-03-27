# this one is like your scripts with argv
def print_two(*args): # asterisk tells python to put arguments into a list []
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# okay, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# Python function checklist:
# 1. Start function with def
# 2. Function name is begins with character and contains char, num, or _
# 3. Open parenthesis right after function name
# 4. Arguments after open parenthesis separated by commas
# 5. Function arguments must be unique
# 6. Close parenthesis and colon ): after arguments
# 7. Indent all lines with exactly four spaces
# 8. End function by removing indents i.e. "dedenting"

# Scott plays around with the use of *args
def print_test(*args):
	for i in args:
		print i

print_test("one","two","three","four")
print_test("one")