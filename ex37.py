# Keyword 'review'

# 1. and -- logical and
if (1 == 1 and 2 == 2):
	do something


# 2. as -- used when interacting with objects
with open("file.txt") as f:
	data = f.read()
	do something with data

# 3. assert -- used to confirm something is true
assert 1 != 2	# This will cause an error

# 4. break -- used to break out of a loop
for letter in 'Python':
	if letter == 'h':
		break  	# This line will stop the loop
	print 'Current letter:", letter

# 5. class -- used to define an object
class employee:
	emp_count = 0
	
	def __init__(self, name):
		self.name = name
		employee.emp_count += 1
	
	def display_employee(self):
		print "Name : ", self.name

# 6. continue -- returns control at the top of the loop
for letter in 'Python':
	if letter == 'h':
		continue	# This will skip the print step for h and begin for n
	print "Current letter:", letter