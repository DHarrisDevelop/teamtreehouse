def disemvowel(word):
	#break the word into a list
	word_list  = list(word)
	#we want to check for vowels, both upper and lower case
	vowel_list = ['a','e','i','o','u','A','E','I','O','U']
	#keep track of if we removed a vowel or not, must set to True so loop will execute first time
	removed = True
	while removed:
		#make sure we don't get in an infinite loop
		removed = False
		for vowel in vowel_list:
			try:
				word_list.remove(vowel)
				removed = True
			except ValueError:
				pass
	word = "".join(word_list)
	return word