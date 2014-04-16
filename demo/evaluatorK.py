"""
evaluatorK.py - Khoa Nguyen - GAOthello
CS 480 Truman State University

This file is no more a part of the system, but shows the work
of one group member.
"""

import board
class Evaluator(object):
    oldFile = "firstGeneration.txt"
    newFile = "new.txt"
    
    FILE_DATA = None
    WEIGHT = None
    
    def readFile(self):
        """ Used in delOneLine to delete the first line in the file """
        theFile = open(oldFile, 'r')
        FILE_DATA = theFile.readlines()
        theFile.close()

    def delOneLine( self ):
        """ Remove the first line of the input file """
        theFile = open( oldFile, 'w')
        for i in range( 1, len(FILE_DATA)):
            theFile.write(FILE_DATA[i])
        theFile.close() 

    def score( self, board ):
        """ Assign the weights from 1D array to the 2D board """
        
        weightedBoard = board
        
        for i in range (0, 4):
            for j in range (0, 4):
                k = evalRow(i)
                weightedBoard[i][j] = weight[k + j]
                    
        for i in range (7, 3):
            for j in range (0, 4):
                if board[i][j] == self.player:
                    k = evalRow(i)
                    weightedBoard[i][j] = weight[k + j - 4]
                    
        for i in range (0, 4):
            for j in range (7, 3):
                k = evalReverse(i)
                k = evalRow(k)
                weightedBoard[i][j] = weight[k + j]
                    
        for i in range (7, 3):
            for j in range (7, 3):
                k = evalReverse(i)
                k = evalRow(k)
                l = evalReverse(j)
                weightedBoard[i][j] = weight[k + l - 4]

        return weightedBoard

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

    def printBoard( self ):
        a = Evaluator.score( self )
        for i in range ( 8 ):
            for j in range ( 8 ):
                print self.board[i][j] ,
