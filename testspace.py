word = "tallie"
user_guesses = ""

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
	for charactors in list(alphabet):
		if charactors in word:
			alphabet = alphabet.replace(charactors," ")
	return alphabet




print "WELCOME TO HANGMAN"
print "\n"
print line_layout() 
print "\n"
print remove_guessed_letter("")

guess1 = "t"

if guess1 in word:
	user_guesses = user_guesses + guess1
	print "You got one!"
	print line_layout()
	print remove_guessed_letter()

