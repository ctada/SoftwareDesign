""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	# strip away header
	f=open(file_name, 'r')
	words=[]
	start = False
	for line in f: 
		if "*** START" in line:
			start = True
		elif start: #moves to line after ***START trigger
			line = string.lower(line) #making everything lowercase
			for word in line:
				word= string.strip(word, string.punctuation) #won't strip punctuation in the middle of the word, i.e. "don't"
			words.extend(line.split()) #using split without an argument removes all whitespace when splitting into words
	return words

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	word_dict = {}

	# counts number of repeats for each word
	for word in word_list: 
		if word in word_dict:
			word_dict[word]+=1
		else:
			word_dict[word] = 1
	top_list = sorted(word_dict, key=word_dict.get, reverse=True)
	return top_list[0:n]

if __name__ == "__main__":
	l= get_word_list('grimm.txt')
	print get_top_n_words(l, 100)