# University of Michigan PyBridge, Part 2
# wordcount.py skeleton code

# Concept and some code borrowed from Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise
Modified from an example in Google's Python class

The main() below is already defined and complete. It calls count_words()
and count_top() functions which you write.


Read the text file and return a dictionary of (word, count) key-value pairs, 
sorted alphabeticallyby word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

Hint on workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure.
When that's working, try for the next milestone.

Optional: it may be useful to define a helper function to avoid code duplication inside
count_words() and count_top().

**Call the script from the command line using the following command format:

python wordcount.py alice.txt alice_counts.csv
"""

import sys


# TODO: Define count_words(infile, outfile) and print_top(filename, n) functions.
#count_words() should take an input filename as its only parameter.
#the input filename (infile) is the filename of the text file you want to count words from.
#count_words() should return a dictionary of (word: count) pairs (hint: you must return this dictionary so that 
#the writeToCsv function can use it in the testing code I've provided. You can completely ignore punctuation
#for this function--just leave any punctuation in words--but make sure you remove all capitalization.

#writeToCsv takes data (a Python dictionary) and outfile (the desired csv filename) as its parameters.
#It writes a csv file of each word, count pair, matching the output of the provded alice_counts.csv exactly.

#count_top takes an input filename and n as its parameters. It does not return anything, but it prints
#the top n words and their corresponding couts to the console. 
#hint: make it easy for yourself--count_top should call your count_words function!




def count_words(infile):

  output = {}
  infile = open(infile, 'r')
  data = infile.readlines()
  
  # +++your code here+++

  return output

def writeToCsv(data, outfile):

  outfile = open(outfile, 'w')

  # +++your code here+++


  outfile.close()

  return None

def count_top(filename, n):

  # +++your code here+++

  return None



#DO NOT MODIFY CODE BELOW THIS LINE 
#This basic code is provided and
# calls the count_words() and count_top() functions which you must define above.

def main():
  infile = sys.argv[1]
  outfile = sys.argv[2]

  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py infile outfile'
    sys.exit(1)

  print "Testing counts \n"
  counts = count_words(infile) 

  print "\n Your top count_words results \n"
  print sorted(counts.items(), key = lambda x: x[1], reverse = True)[0:10]
  print "\n Desired results \n"
  print "('the', 1605), ('and', 766), ('to', 706), ('a', 614), ('she', 518), ('of', 493), ('said', 421), ('it', 362), ('in', 352), ('was', 333)"

  print "\n Testing writeToCsv \n"
  writeToCsv(counts, outfile)

  print "Testing count_top(10) \n"
  count_top(infile, 10) 

  print "\n Desired results \n"
  print "('the', 1605), ('and', 766), ('to', 706), ('a', 614), ('she', 518), ('of', 493), ('said', 421), ('it', 362), ('in', 352), ('was', 333)"

if __name__ == '__main__':
  main()
