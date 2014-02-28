def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	print words
	pass

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
	pass

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word
	pass

def print_last_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(-1)
	print word
	pass

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(sentence)
	pass

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	pass

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	pass


#break_words("today is good day!")
#
#a = sort_words("taday is good day!")
#b = sort_words("32153151")
#print a
#print b
#
#print_first_word(["today is good day!",'123',"this",'332'])
#c = ["this is one","this is two",3,4,5]
#print_last_word(c)
#print c

print sort_sentence("today is good day!")