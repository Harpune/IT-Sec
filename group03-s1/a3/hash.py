#!/usr/bin/python2
###
# Note: this code was modified to more closely resemble java.
########
# This hash function computes a simplistic hash of any file.
# input:  arbitrary binary file
# output: four bytes
########
# Description of the hash function:
# the rightmost two bytes are determined by the length of the lines in the file.
# the next four bytes are determined by the entire contents of the file and previous step.
# the last two bytes are set by the amount of lines in the file and the previous step.
# see also the code below
########

#parse argument
import sys

#exactly 2 arguments
if len(sys.argv) != 2 or not sys.argv[1]:
	print "please provide exactly one file name as argument"
	sys.exit(1)


counter = 0
lengthList = []
sumList = []

# try/except for sensible error-handling
try:
	#open the file that needs to be hashed, parse the necessary info
	with open(sys.argv[1], 'rb') as file:
		for line in file:
			counter = counter + 1

			value = 0
			for character in line:
				value = value + ord(character)
			sumList.append(value)
			# ord('c') returns the number used to represent the given character:
			# can be either ASCII or unicode.

			lengthList.append(len(line))
except IOError, e:
	print "Error while reading file: %s"%(e)
	sys.exit(1)

# compute the hash itself:
hash = counter * 0x01000000
for item in sumList:
	hash = hash + item * 0x00000100
for item in lengthList:
	hash = hash + item * 0x00000001
	hash = hash & 0xFFFFFFFF
print "%08x"%(hash)
