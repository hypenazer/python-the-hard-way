# prints 'Mary had a little lamb' on a single line
print "Mary had a little lamb."
# prints 'Its fleece was white as snow'
print "Its fleece was white as %s." % 'snow'
# prints 'And everywhere that Mary went.'
print "And everywhere that Mary went."
# prints 10 periods i.e. ..........
print "." * 10 # what'd that do?

# sets variables end1 - end12
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# prints end1 - end12 on a single line; the comma adds a space character
# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# what happens if I substitute a plus sign with a comma?
print end1 + end2 + end3 + end4 , end5 + end6  # prints "chee se"

#print , end7 + end8 + end9 + end10 + end11 + end12 # I cannot put a comma at the start
print "" , end7 + end8 + end9 + end10 + end11 + end12 # but I *can* lead with a an empty string.


# Python style is to limit lines to 80 characters.
# I've limited the page guide to 80 characters in textwrangler
# Method is TextWrangler > Preferences > Appearance > Page guide at [ ] chars