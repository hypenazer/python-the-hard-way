def break_words(stuff):
	# Three double quotes documents the function for help(break_words)
	"""This function will break up words for us."""
	# Split the string into a list using ' ' as the separator
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	# Use built-in function "sorted" to sort the list help(sorted) for details
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping if off."""
	# Treats words list as a stack. Pops 0 position off stack and puts in 'word'
	# Python words list loses its first value even though pop is in function?
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping if off."""
	# Negative pop values mean to start at end; value must be in range
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	# Use break_words to put sentence into a list
	words = break_words(sentence)
	# Use print_first_word to print the first word in the list/sentence
	print_first_word(words)
	# Use print_last_word to print the last word in the list/sentence
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	# Use sort_sentence to convert sentence to list and sort list
	words = sort_sentence(sentence)
	# Use print_first_word to print the first word in the list/sentence
	print_first_word(words)
	# Use print_last_word to print the last word in the list/sentence
	print_last_word(words)


# Test the script using __name__ = "__main__"
if __name__ == "__main__":
	sentence = "All good things come to those who wait."
	words = break_words(sentence)
	print words
	sorted_words = sort_words(words)
	print sorted_words
	print_first_word(words)
	print_last_word(words)
	print words
	print_first_word(sorted_words)
	print_last_word(sorted_words)
	print sorted_words
	sorted_words = sort_sentence(sentence)
	print sorted_words
	print_first_and_last(sentence)
	print_first_and_last_sorted(sentence)
