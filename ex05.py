# variable names must start with non-numeric
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_centimeters = height * 2.54
weight_kilograms = weight * 0.453592

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %04d inches tall." % height  #this will print leading 0s up to 4 places
print "He's %4d inches tall." % height # this will print leading space characters up to 4 places
print "He's %06.2f inches tall." % height #this will print 6 places with 2 after decimal and pad with 0s

print "He's %.2f inches tall." % height #this will print 2 places after the decimal
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "He's %04d centimeters tall." % height_centimeters
print "He's %f kilograms heavy f." % weight_kilograms

print "He's %r kilograms heavy r." % weight_kilograms # %r invokes repr() function -- "Return a string containing a printable representation of an object."
#it's unclear how to modify decimals displayed using %r
print "He's %0.22r kilograms heavy r." % weight_kilograms # %r invokes repr() function -- "Return a string containing a printable representation of an object."


# this line is tricky try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)



# full set of string formatting:
# https://docs.python.org/2/library/stdtypes.html#string-formatting