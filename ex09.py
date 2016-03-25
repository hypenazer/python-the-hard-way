# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
# \n is new line character just like php
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

# it appears three double-quotes make the string a literal
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5 or 6.
"""

# what about special characters?
print """
There's something going on here. %s
With the three double-quotes. #what happens? %05d
We'll be able to type as much as we like.
Even 4 lines if we want, or 5 or 6.
""" % ('test' , 5)
# yes comments are treated as literal; but formatting is honored