def list_builder_while(x, incr):
	i = 0
	numbers = []
	while i < x:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + incr
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	return numbers

def list_builder_for(x, incr):
	numbers = []
	for i in range(0, x / incr):
		print "At the top i is %d" % i
		numbers.append(i * incr)
		
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	return numbers


numbers = list_builder_for(12, 3)


print "The numbers: "

for num in numbers:
	print num