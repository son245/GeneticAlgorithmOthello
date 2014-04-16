# Since we cannot generate first generation using GA, 
# this random generator works on it
"""
randomGenerator.py - Tian Zheng - GAOthello
CS 480 Truman State University
"""

from random import randint

f = open('firstGeneration', 'w')

# Generate 20 lines with an array of 16 random numbers in each line
for i in xrange(20):
	board = []
	for j in xrange(16):
		seed = randint(-100,100)
		board.append(seed)
	f.write(str(board))
	f.write('\n')
    
f.close()