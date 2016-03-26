# The comma on this line strips the new line character
# The user prompt is on the same line
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# raw_input can also be used to prompt the user like this:
weight2 = raw_input("How much do you weigh? ")

# or prompt the user on a new line like this:
weight3 = raw_input("How much do you weigh? \n")

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

# notes:
#  - raw_input() will always return a string
#  - prompting for numbers requires converting to number like: int(raw_input())