# set the formatter variable
formatter = "%r %r %r %r"

# use the formatter string to format the integers: 1, 2, 3, 4
print formatter % (1, 2, 3, 4)
# use the formatter string to format the strings: "one", "two", "three", "four"
print formatter % ("one", "two", "three", "four")
# use the formatter string to format True, False, False, true
print formatter % (True, False, False, True)

# Ha!  This does the integer format of True, False, False, True
print "%d %d %d %d" % (True, False, False, True)

# use the formatter string to format the string contained in formatter
print formatter % (formatter, formatter, formatter, formatter)

# Use the formatter string to format the strings "I had...", "that you..", etc.
# I assume Python prints with single quotes (')
# Unless the string contains a single quote
# Then it prints strings with double quotes (")
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

# this won't have double quotes (I'm guessing)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didnt sing.", 				# removed single quote from this line.
	"So I said goodnight."
)