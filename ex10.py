tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


print "this is a\vvertical tab"

for x in range(0,10):
	for i in ["/","-","|","\\","|"]:
#		print "%s\r" % i,  #carriage return character doesn't work
		print "%s\n" % i,
		
# Python escape characters:
# \\ Backslash (\)
# \' Single-quote (')
# \" Double-quote (")
# \a ASCII bell (BEL)
# \b ASCII backspace (BS)
# \f ASCII formfeed (FF)
# \n ASCII linefeed (LF)
# \N{name} Character named name in the Unicode database
# \r Carriage return(CR)   <-- I wasn't able to get this to work on osx
# \t Horizontal Tab (TAB)
# \uxxx Character with 16-bit hex value xxxx
# \Uxxxxxxxx Character with 32-bit hex value xxxxxxxx
# \v ASCII vertical tab (VT)
# \ooo character with octal value ooo
# \xhh character with hex value

