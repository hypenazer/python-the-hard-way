def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5  + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def addition(one, two):
	print "The sum of %d and %d is: %d" % (one, two, one + two)


def multiplication(one, two):
	print "The product of %d and %d is: %d" % (one, two, one + two)

def subtraction(one, two):
	print "The difference of %d and %d is: %d" % (one, two, one - two)

def division(one, two):
	print "The quotient of %d and %d is: %0.2f" % (one, two, 1.0 * one / two)

addition (1, 4)
multiplication (1, 4)
subtraction (1, 4)
division (1, 4)

def addition_many(*args):
	x = 0
	st = '0'
	for i in args:
		x += i
		st = st + ' + ' + str(i)
	print st + ' = ' + str(x)
	
addition_many(1, 3, 12, 14, 0, -1)




