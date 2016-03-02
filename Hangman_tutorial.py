import random 

#hangman word list
words = ["orange", "apple", "banana", "grapefruit", "lemon", "tomato"]

#computes length of word list, eg. how many items in said list
word_list_length = len(words)-1 
#picks a random integer within the length of the word list
chosen_word_index = random.randint(0, word_list_length)
#selects a word from the wordlist using the random integer computed above
chosen_word = (words[chosen_word_index])

#print out underscores!
underscores = ""
for i in chosen_word:
	underscores += "__ "

#store user_guesses
user_guesses = ""
user_guesses = raw_input("Pick a letter! ")

#letter guess or word guess
if len(user_guesses) > 1:
	print "word" #typed in a word
else: 
	#typed in letter