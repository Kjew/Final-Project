word = "tallie"


#removes letter from alphabet once guessed
def remove_guessed_letter(word): #remove letter once guessed
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for charactors in list(alphabet):
		if charactors in word:
			alphabet = alphabet.replace(charactors," ")
	return alphabet

guess1 = "t"

print remove_guessed_letter()