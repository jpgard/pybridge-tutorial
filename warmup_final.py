#Code written by Josh Gardner, UMSI

"""
Warmup Exercise

Try each of the exercises below to get yourself warmed up for PyBridge 2!
You will need each of these skills to be prepared for the task we're working on today.

This code consists of a series of functions that you need to complete in order to
produce the desired result. The 'main' script will call each of these functions,
and if you produce the desired output, move on to the next function.

In some cases, you will need to delete the 'return None' and replace it with what you'd like the function to return.

Some of the functions have code already there for you--don't delete it unless you're positive you don't want it.

Don't cheat by just copying the desired output :)
"""


def addone(input):

	#this function should take a number as input, and add one to whatever number it receives as input.
	#If it receives something other than a number, it should print "invalid input".

	# +++your code here+++


	# +++end your code+++

	return None


	


def printLines(infile, n):

	#this function should read an input text file, and individually print its first n
	#lines to the console. Don't worry about invalid input files for this function.
	#note: you should use print for this function--leave the 'return None' statement at the bottom.

	

	input = open(infile, 'r')
	data = input.readlines()
	
	# +++your code here+++

	# +++end your code+++

	return None
	

def lowerLineList(infile, n):
	#this function should read an input text file, and return a list containing the words of the nth line
	#as output, with all words/letters as lowercase (so you should use return, NOT print in this function!) 
	#Don't worry about invalid input files for this function.

	# +++your code here+++

	input = open(infile, 'r')
	data = input.readlines()
	print data[n-1].lower().split()
		
	

	return None
	# +++end your code+++

def dictPlusOne(input):

	#this function should take a Python dictionary as its input, and it should add one
	#to the value of each element in the dictionary.
	#hint: try using dict.items() -- you'll need to use a for loop!
	#note: this will return items in a random order when you print them; that's fine as long as the numbers are correct.


	# +++your code here+++

	for k,v in input.items():
		input[k] += 1

	return input
	# +++end your code+++

def main():

	print "Testing addone(5)" + '\n'
	print addone(5)
	print '========================'
	print '\n'
	

	print "Testing printLines(republican_debate.txt, 10)" + '\n'
	printLines('republican_debate.txt', 10)
	print '========================'
	print '\n'

	print "Testing lowerLineList(republican_debate.txt, 565)" + '\n'
	lowerLineList('republican_debate.txt', 565)
	print '========================'
	print '\n'

	print "Testing dictPlusOne with testdict = {'first' : 1, 'second' : 25, 'third' : '100'}" + '\n'
	testdict = {'first' : 1, 'second' : 25, 'third' : 100}
	print dictPlusOne(testdict)
	print '========================'

if __name__ == '__main__':
	main()