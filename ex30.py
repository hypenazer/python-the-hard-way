people = 30
cars = 30
trucks = 20

# If we have more cars than people and we have fewer trucks than people
if cars > people and trucks < people:
	# Print 'We should take the cars.'
	print "We should take the cars."
# If we have fewer cars than people
elif cars < people:
	# Print 'We should not take the cars.'
	print "We should not take the cars."
# If neither of the above are true
else:
	# Print 'We can't decide.'
	print "We can't decide."

# If we have more trucks than cars
if trucks > cars:
	# Print That's too many trucks
	print "That's too many trucks."
# Otherwise, if we have fewer trucks than cars
elif trucks < cars:
	# Print Maybe we could takek the trucks.
	print "Maybe we could take the trucks."
# If neither of the above are true
else:
	# Print We still can't decide
	print "We still can't decide."

# If we have more people than trucks
if people > trucks:
	# Print Alright, let's just take the trucks.
	print "Alright, let's just take the trucks."
# Otherwise, print Fine, let's stay home then.,
else:
	print "Fine, let's stay home then."
	
# Study Drills
#
# 1. elif and else run alternate blocks of code if condition evaluates as False
# 2. 
