letter = "j"

hangword = "mik"

if letter in hangword:
	print "Yes! Letter is in the word"	
elif letter not in hangword:
	print "Wrong!"

num_misses = 0
the_guess = 0
valid_characters = "abcdefghijklmnopqrstuvwxyz"
user_guesses = "i"
the_mask = ""
secret_words = ["mik"]

num_user_guesses = 0
user_guesses = "i"
word = "nincompoop"

#prints lines, 
def line_layout():
	line_layout = ""
	for letter in range(len(word)): #for every letter in word
	    if(user_guesses.find(word[letter]) >= 0): #s.find(x) returns the integer index of where x is found in s(tring), returns -1 if x not found.
	       line_layout += " " + word[letter] + " " #in word!
	    else:
	       line_layout += " _ " #not in word
	return line_layout

#removes letter from alphabet once guessed
def remove_guessed_letter(word): #remove letter once guessed
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for letter in list(alphabet):
		if letter in word:
			alphabet = alphabet.replace(letter," ")
	return alphabet


print "WELCOME TO HANGMAN"
print "\n"
print line_layout() 
print "\n"
print remove_guessed_letter("")




