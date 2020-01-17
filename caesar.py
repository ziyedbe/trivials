def mostuserchar(ch):
	#This dictionary is used to count every letter in the chain
	chars = {"a":0,
		"b":0,
		"c":0,
		"d":0,
		"e":0,
		"f":0,
		"g":0,
		"h":0,
		"i":0,
		"j":0,
		"k":0,
		"l":0,
		"m":0,
		"n":0,
		"o":0,
		"p":0,
		"q":0,
		"r":0,
		"s":0,
		"t":0,
		"u":0,
		"v":0,
		"w":0,
		"x":0,
		"u":0,
		"z":0}

	keys=list(chars.keys())
	for i in ch:
		if(i.lower() in keys): #We made this condition to avoid characters such as space and ., etc
			#We add value to the dictionary 
			chars[i.lower()]=chars[i.lower()]+1
	values = list(chars.values())
	return keys[values.index(max(values))] # We returned the index of the most used letter

def caesar(ch):
	#We start by getting the most used letter in out string
	letter = mostuserchar(ch)
	output=""
	#We calculate the shift because we knows that the most used letter in english is e
	shift = ord(letter)-ord("e")
	
	for i in ch:
		if i.lower() in "abcdefghijklmnopqrstuvwxyz":
			#This is the tricky part
			#The order of letters doesn't start from 1 but 97 which is the order of "a"
			#So first we calculate the new letter this way ord(i)-shift-ord("a")
			#Let's have an example so you can understand
			#let's consider "b" with order 98, a 10 shift
			#98 - 10 = 88
			#we then calculate 88-ord("a")=-9 to bring it to the range of [-26,26]
			#-9%26=17
			#17 + ord("a")=17+97=114
			#chr(114)="r"
			output+=chr(((ord(i)-shift-ord("a"))%26)+ord("a"))
		else:
			#This else is to keep spaces and special characters
			output+=i
	return output
