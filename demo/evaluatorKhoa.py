"""
evaluatorK.py - Khoa Nguyen - GAOthello
CS 480 Truman State University

This file is no more a part of the system, but shows the work
of one group member.
"""

from config import BLACK, WHITE, EMPTY

class eval:
    """ Open file, read lines to a list, close file
        Evaluate.
        open file again, write every line except first line
        back to the file, close file."""
    def __init__(self, firstFile, secondFile):
        self.firstFile = firstFile
        self.secondFile = secondFile
        
    def readFile(self):
        """ Used in delOneLine to delete the first line in the file """
        theFile = open(self.firstFile, 'r')
        lines = theFile.readlines()
        theFile.close()
        return lines

    def delOneLine(self, listLines):
        """ Remove the first line of the input file """
        theFile = open(self.firstFile, 'w')
        for i in range(1, len(listLines)):
            theFile.write(listLines[i])
        theFile.close() 

    def getFirstLine(self):
        """ return first line as a list of given weight """
        lines = eval.readFile(self)
        theList = lines[0].split("\n")
        theList = theList[0].split(',')
        for i in range(len(theList)):
            theList[i] = int(theList[i])

        return theList

    def writeFile(self):
        """ Write the weight and the 17th number (sum of weights into
            another file """
        theFile = open(self.secondFile, 'w')
        theWeight = eval.getFirstLine(self)
        for i in range(len(theWeight)):
            theFile.write(str(theWeight[i]))
            theFile.write(",")
        theFile.write(score( self, board,  player))

        theFile.close()
        
        
    def evalReverse(self, inNum):
        if inNum == 7: actual == 0
        elif inNum == 6: actual == 1
        elif inNum == 5: actual == 2
        else: actual == 3
        return actual

    def evalRow(self, row):
        if row == 0: actualRow = row
        elif row == 1: actualRow = row + 4
        elif row == 2: actualRow = row + 8
        else: actualRow = Row + 12
        return actualRow
    
    def score( self, board,  player):
        """ Use the weight array and return a score of the sum of weights
            player = the color of player
            board = the board used in scoring"""
        
        self.player = player
        score = 0

        ## Evaluate the board using the weight,
        ## taking into account the symmetry
        weight  = getFirstLine()
        for i in range (0, 4):
            for j in range (0, 4):
                if board[i][j] == self.player:
                    k = evalRow(i)
                    score += weight[k + j]
                    
        for i in range (7, 3):
            for j in range (0, 4):
                if board[i][j] == self.player:
                    k = evalRow(i)
                    score += weight[k + j - 4]
                    
        for i in range (0, 4):
            for j in range (7, 3):
                if board[i][j] == self.player:
                    k = evalReverse(i)
                    k = evalRow(k)
                    score += weight[k + j]
                    
        for i in range (7, 3):
            for j in range (7, 3):
                if board[i][j] == self.player:
                    k = evalReverse(i)
                    k = evalRow(k)
                    l = evalReverse(j)
                    score += weight[k + l - 4]
        return score

""" to use this, first create eval object,
then use writeFile() to write find the score and write into a new file
call delOneLine to delete the first line in the old file.
"""
