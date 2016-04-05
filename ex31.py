print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake.  What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off.  Good job!"
	elif bear == "2":
		print "The bear eats your legs off.  Good job!"
	else:
		print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
	print "You are at the top of a dark staircase.  A lightswitch is to your right."
	print "1. Decend the stairs"
	print "2. Toggle lightswitch"
	print "3. Turn around"
	
	stairs = raw_input("> ")
	
	if stairs == "1":
		print "The first stair breaks under your weight.  You fall into a pool of shaving cream."
	elif stairs == "2":
		print "The stairway illumates.  At the base is a wolfe mauling a parrot."
	else:
		print "You become dizzy, fall down the stairs and die."

else:
	print "You stumble around and fall on a knife and die.  Good job!"
