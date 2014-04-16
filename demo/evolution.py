from random import randint
import random
"""
evolution.py - Son Nguyen - GAOthello
CS 480 Truman State University
This is the genetic algorithm implementation file for othello game.
xThe other part of the game is based on Humberto Henrique Campos Pinheiro's
othello game on GitHub.
"""
# Requirement:
# read the n member in the population
# decide to keep max of 3 and min of 1 child for later generation
# save the child(s) into memory, proceed to evlution with n - s(select)
# remaining childs
# because the terminal test is hard enough, we will play it again a constant 
# AI to see all the improvement and learning capability of the algorithm
# [00, 01, 02, 03]
# [10, 11, 12, 13]
# [20, 21, 22, 23]
# [30, 31, 32, 33]

#INPUT
f = open("output.txt", "r+")
l = 0
list = []
while(l < 20):
   a = f.readline()
   list.append(a)
   l = l + 1

i = 0
j = 1
temp = " "
thisGeneration = []
while(i < 20):#indicate the number of child in the generation
#restart j to 1 after each child
   child = []
   while(list[i][j] != "]"):
      if list[i][j] != "," and list[i][j] != " ":
         if temp == " ":
            temp = list[i][j]
            j = j + 1
         else:
            temp = temp + list[i][j]
            j = j + 1
      elif list[i][j] == "," :
         child.append(temp)
         temp = " " 
         j = j + 1
      else:
         j = j + 1
   child.append(temp)
   thisGeneration.append(child)
   temp = " "
   i = i + 1
   j = 1
print thisGeneration[0][16]

# SELECTION
localMax = -100#smallest possible
maxIndex = 0
nearMaxIndex = 0
for i in xrange(20):
   if thisGeneration[i][16] > localMax:
      localMax = thisGeneration[i][16]
      nearMaxIndex = maxIndex
      maxIndex = i

print maxIndex
print nearMaxIndex

#will keep max and near max for next generation, the rest go through evolution
newGeneration = []
thisGeneration[maxIndex].pop()
thisGeneration[nearMaxIndex].pop()
newGeneration.append(thisGeneration[maxIndex])
newGeneration.append(thisGeneration[nearMaxIndex])
evolution = []
for i in xrange(20):
   if i == maxIndex:
      continue
   elif i == nearMaxIndex:
      continue
   else: 
      evolution.append(thisGeneration[i])

#remove the heuristics of members going through evolution
for i in xrange(18):
   evolution[i].pop()

#EVOLUTION
CROSS_OVER_RATE = 0.5
MUTATION_RATE = 0.5
CROSS_OVER_POINT = 7

random.shuffle(evolution)
print "before evolution"
print evolution
for i in xrange(10):#do mutation for first ten
   randomIndex = randint(0,15)
   evolution[i][randomIndex] = randint(-100,100)

#cross over
print "after mutation"
print evolution
temp = 0
for i in xrange(10,14):
   index = CROSS_OVER_POINT
   while(index < 16):
      temp = evolution[i][index] 
      evolution[i][index] = evolution[i+4][index]
      evolution[i+4][index] = temp
      index = index + 1
print "after evolution"
print evolution

for i in xrange(18): 
   newGeneration.append(evolution[i])

print "new Generation"
print newGeneration



file = open("input.txt","w")
for i in xrange(20):
   file.write("[")
   for j in xrange(16):
      file.write(str(newGeneration[i][j]))
      if j != 15:
         file.write(", ")
   file.write("]")
   file.write('\n')
f.close()
open('output.txt', 'w').close()
file.close()