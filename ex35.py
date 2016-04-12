from sys import exit

def gold_room():
	""" Describe room and ask user how much gold to take """
	print "This room is full of gold.  How much do you take?"
	
	while True:
		try:
			choice = raw_input("> ")
 			how_much = int(choice)
			# If we get here, we know int conversion is successful.
			break
		except:
			# If we get here, we know try step failed
			print "Man, learn to type a number."
			gold_room()
	
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)	# Close application without error
	else:
		dead("You greedy bastard!")

def bear_room():
	""" Describe bear room and prompt user for input """
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door.  You can go through it now."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def cthulhu_room():
	""" Describe cthulhu room and prompt user for input """
	print "There you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	choice = raw_input("> ")
	
	if "flee" in choice:
		# Return to the start of the program
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		# Return user to the cthulhu room
		cthulhu_room()

def dead(why):
	""" Print reason for death followed by 'good job' and exit """
	print why, "Good job!"
	exit(0)

def start():
	""" Describe the start of the game and prompt the user for input. """
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()