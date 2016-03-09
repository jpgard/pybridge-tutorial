#Code written by Josh Gardner, UMSI

"""
Warmup Exercise

Try each of the exercises below to get yourself warmed up for PyBridge 2!
You will need each of these skills to be prepared for the task we're working on today.

This code consists of a series of functions that you need to complete in order to
produce the desired result. The 'main' script will call each of these functions,
and if you produce the desired output, move on to the next function.

Don't cheat by just copying the desired output :)
"""


def addone(input):

	#this function should take a number as input, and add one to whatever number it receives as input.
	#If it receives something other than a number, it should print "invalid input".

	# +++your code here+++

	return input + 1


	# +++end your code+++


def printLines(infile, n):

	#this function should read an input text file, and individually print its first n
	#lines to the console. Don't worry about invalid input files for this function.
	#note: you should use print for this function--leave the 'return None' statement at the bottom.

	# +++your code here+++

	input = open(infile, 'r')
	data = input.readlines()
	for x in data[0:n+1]:
		print x

	return None
	# +++end your code+++

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

def writeToCsv(input, outfile):
	#this function should take a Python dictionary as its input, and it
	#should write each (key, value) pair in the dictionary to
	#a .csv file with the name specified by outfile.
	#Assume that the value for each entry is a single item (not a list or a tuple of items).
	#hint: a csv is just a series of entries separated by commas, with
	#a newline character at the end.
	#Here's what a sample row with three cells might look like:
	#'trump, 25% \n'

	outfile = open(outfile, 'w')

	for k,v in input.items():
		outfile.write(str(k) + ' ,' + str(v) + '/n')


	return None


#NO NOT MODIFY CODE BELOW THIS LINE

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

	print "Testing writeToCsv(testdict)"
	writeToCsv(testdict)
	print '========================'


if __name__ == '__main__':
	main()