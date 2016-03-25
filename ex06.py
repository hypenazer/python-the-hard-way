# set x equal to 'there are 10 types of people.' is replaced %d with 10
x = "There are %d types of people." % 10

# set binary and do_not
binary = "binary"
do_not = "don't"

# use the values for binary and do_not to set y
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# %r prints strings with surrounding quotes
print "I said: %r." % x  # print x with single quotes

# %s prints strings with no surrounding quotes
print "I said: %s" %x # print x with no quotes
print "I also said: '%s'." % y # print y with single quotes

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# use hilarious to replace the %r field in joke_evaluation
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# The + operator for strings must be concatenate
print w + e 	# concatenate strings w and e

# Python variables are case sensitive
#print W + E		# this generates an error

