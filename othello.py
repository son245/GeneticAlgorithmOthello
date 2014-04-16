#!/usr/bin/env python
"""
othello.py Humberto Henrique Campos Pinheiro
Game initialization and main loop

This file has been modified by Tian Zheng for research purpose.

"""

import os
import pygame
import ui
import player
import board
from config import BLACK, WHITE

import sys, os
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')


class Othello:
    """
    Game main class.
    """
    def __init__( self ):
        """ Show options screen and start game modules"""
        # start
        self.gui = ui.Gui()
        self.board = board.Board()
        self.get_options()
        self.counter = 0

    def get_options( self ):
        # set up players
        player1, player2, level = self.gui.show_options()
        if player1 == "human":
            self.now_playing = player.Human ( self.gui, BLACK )
        else:
            self.now_playing = player.Computer ( BLACK, level+3 )
        if player2 == "human":
            self.other_player = player.Human ( self.gui, WHITE )
        else:
            self.other_player = player.Computer ( WHITE, level+3 )

        self.gui.show_game()
        self.gui.update(self.board.board, 2, 2)


    def run ( self ):
        clock = pygame.time.Clock()
        self.counter = self.counter + 1
        while True:
            clock.tick( 60 )
            if self.board.game_ended():
                whites, blacks, empty = self.board.count_stones()
                if whites > blacks:
                    winner = WHITE
                elif blacks > whites:
                    winner = BLACK
                else:
                    winner = None
                break
            self.now_playing.get_current_board ( self.board )
            if self.board.get_valid_moves( self.now_playing.color ) != []:
                score, self.board = self.now_playing.get_move()
                whites, blacks, empty = self.board.count_stones()
                self.gui.update( self.board.board, blacks, whites)
            self.now_playing, self.other_player = self.other_player, self.now_playing
        self.gui.show_winner( winner, blacks-whites)
        pygame.time.wait( 1000 )
        if self.counter <= 20:
            
            f = open("input.txt", "r+")
            line = f.readline()
            f.close()
            f = open("output.txt", "a")
            line = line[:-2]
            seq = (line, ", ", str(blacks-whites), "]")
            f.write(''.join(seq))
            f.write('\n')
            f.close()

            with open('input.txt', 'r') as fin:
                data = fin.read().splitlines(True)
            with open('input.txt', 'w') as fout:
                fout.writelines(data[1:])
        
        if self.counter == 20:
            os.system("python evolution.py")
            counter = 0

        self.restart()

    def restart( self ):
        self.board = board.Board()
        self.get_options()
        self.run()

def main():
    game = Othello()
    game.run()

if __name__ == '__main__':
    main()


