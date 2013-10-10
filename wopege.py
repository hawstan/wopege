#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ------
# Word Permutation Generator (WoPeGe)
# version 0.1
# created 2010-09-23
# author Stanley Hawkeye
# ------
# Thanks to the person who originally helped me with this algorithm.
# ------
# Options:
# required:
#    -o <output file>
#    -l <minimum amount of characters>
#    -r <maximum amount of characters>
# oprional:
#    -w <charlist file> - use charlist file as the sourse of characters used
#        for generating words, one character per line, "characters" can be more
#        than 1 actual character (that is letter) long
#        Tested only for ASCII characters.
#    -v - verbose
# ------

# use basic a-z alphabet as default
charset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'i', 'p', 'o', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import getopt
import sys
import codecs

outputName = None
output = None

minlen = None
maxlen = None

verbose = False

charlistFile = None

options, args = getopt.getopt(sys.argv[1:], 'o:l:r:w:v')

for key, value in options:
	if key == "-o":
		outputName = value
	elif key == "-w":
		wordlistFile = value
	elif key == '-l':
		minlen = int(value)
	elif key == "-r":
		maxlen = int(value)
	elif key == "-v":
		verbose = True
#

if minlen == None:
	print("No minimal lenght (-l)")
	exit()
#

if maxlen == None:
	print("No maximal length (-r)")
	exit()
#

if minlen > maxlen:
	print("Minimal length (-l) is greater than maximal length (-r)")
	exit()
#

if outputName == None:
	print("No output file (-o)")
	exit()
#

if charlistFile != None:
	print("Using charlist file '"+wordlistFile+"'.")
	try:
		cl = open(charlistFile, "r")
		charset = []
		line = cl.read
		for line in wl:
			line = line[0:-1]
			if len(line) == 0:
				continue
			charset.append(line)
		wl.close()
	except IOError:
		print("Cannot read wordlist file")
		exit()
#

try:
	output = open(outputName, "w")
except OSError:
	print("Cannot open output file:")
	exit()
#

print("Starting generation.")
total = 0
last_character_index = len(charset)-1
for length in range(minlen,maxlen+1):
		permutations = (last_character_index+1)**length
		if verbose:
			print(" Generating",str(permutations),"words of length",str(length))
		local_total = 0
		
		word_by_index = [ 0 for i in range(length) ]

		for i in range(permutations-1):
				word = "".join(map( (lambda x:charset[x]) , word_by_index ))
				print(word,file=output)
				local_total = local_total + 1
				j = length - 1
			   
				while( word_by_index[j] ==  last_character_index ):
						word_by_index[j] = 0
						j = j - 1
				word_by_index[j] = word_by_index[j] + 1
				if verbose and (local_total % 20000 == 0):
					print("  ",str(local_total),"/",str(permutations),"completed")
		total += local_total
output.close()
print("Done, total of",str(total),"words have been generated.")
