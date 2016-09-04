letter_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_space = letter_upper + letter_upper.lower() + ' \t\n'

def get_dict():
	f = open('dictionary.txt','r')
	eng_words = {}
	dict_words = f.read().split('\n')
	for word in dict_words:
		eng_words[word] = None

	f.close()

	return eng_words

eng_words = get_dict()

def get_eng_count(msg):
	msg = msg.upper()
	msg = remove_non_letters(msg)
	msg_words = msg.split()

	if(msg_words == []):
		return 0.0

	matches = 0
	for word in msg_words:
		if word in eng_words:
			matches = matches + 1

	return float(matches)/len(msg_words)


def remove_non_letters(msg):
	no_character = []
	for word in msg:
		if word in letter_space:
			no_character.append(word)

	return ''.join(no_character)


def check(msg, letter = 60, characters = 80):
	lcount = get_eng_count(msg) * 100

	only_letter = remove_non_letters(msg)

	ccount = len(only_letter)

	ccount = (ccount/len(msg)) * 100

	return (lcount>= letter and ccount>=characters)
