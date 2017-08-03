from TOAHModel import TOAHModel, Cheese, IllegalMoveError
import tkinter as TI
import time
# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap,
# Dustin Wehr, Brian Harrington, Harri Pahirathan
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Summer 2017.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""
ConsoleController: User interface for manually solving Anne Hoy's problems
from the console.

move: Apply one move to the given model, and print any error message
to the console.
"""
"""
Harri Pahirathan
Assignment 2
2017-07-31
ENJOY!
"""


def move(model: TOAHModel, origin: int, dest: int):
    '''
    Module method to apply one move to the given model, and print any
    error message to the console.

    model - the TOAHModel that you want to modify
    origin - the stool number (indexing from 0!) of the cheese you want
             to move
    dest - the stool number that you want to move the top cheese
            on stool origin onto.
    '''
    # calls move method from toahmodel
    model.move(origin, dest)


class ConsoleController:

    def __init__(self: 'ConsoleController',
                 number_of_cheeses: int, number_of_stools: int):
        """
        Initialize a new 'ConsoleController'.

        number_of_cheeses - number of cheese to tower on the first stool,
                            not counting the bottom cheese acting as stool
        number_of_stools - number of stools, to be shown as large cheeses
        """
        # Representation Invarient
        # self._game the model of the players game
        # self._finshed_game is the compplete model
        # self._game will start with all the cheese in first stool
        # self._finshed_game will have all the cheese in last stool
        # both models are created by using the TOAH Class in which
        # the container are nested list, each repersentig a stool
        # creates the game model for the number of stools wanted
        self._game = TOAHModel(number_of_stools)
        # fills the game model with the number of cheese wanted
        self._game.fill_first_stool(number_of_cheeses)
        # creates a finshed version fo game model
        self._finshed_game = TOAHModel(number_of_stools)
        # adds the cheese to first stool of finshed game
        self._finshed_game.fill_first_stool(number_of_cheeses)
        # switchs first with last stool so it has final product
        self._finshed_game._stools[-1] = self._finshed_game._stools[0][:]
        # removes everything from first stool so its compelete solution
        self._finshed_game._stools[0] = []

    def play_loop(self: 'ConsoleController'):
        '''
        Console-based game.
        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provded to print a representation of the current state of the game.
        '''
        # the instructions as well as rules
        print('''
        Ladies and Gentlemen! Its Time to play TOWER OF CHEESE!!!
        With your Host today, Mr.DEBUGGER!!!
        Now Heres what will happend:
        1st: You will have to enter 2 numbers seperated by a '/' like so
        0/1. The first number represents the stool with the cheese you want to
        move and the second number is the stool you want that cheese to go to.
        2nd: You must have NO spaces, brackets, letters or etc when entering
        the numbers. Just two numbers seperated by a foward slash /
        3rd: You'll have to do this until you complete it once you've got
        the right answer, you'll be rewarded with a congratualtions from
        MR.DEBUGGER HIMSELLLFF!!!
        4th: If you wanted to quit since the game is so intense you can
        just type 'quit' as one of your moves.
        5th: The first stool is 0, second stool is 1 and etc...

        Thanks for playing! Rules follow bellow:

        Rules:
        - bigger cheese cant be stack on top of smaller ones
        - one move per turn
        ''')
        # this will hold the input of what move they do
        type_move = ''
        # will check is the game is complete or if the user had type quit
        # this will keep looping until the user has quit or completed
        # the game
        while((self._game != self._finshed_game) and (type_move != 'quit')):
            # prints the current game model
            print(self._game)
            # takes the input of the move want to do
            # proper format is num_of_stool_with_cheese/to_stool
            type_move = input('Enter move here: ')
            # as long as the person does not quit it will take the move input
            # and see if its valid and perform it
            if type_move != 'quit':
                # it will try it and if its invalid it will print try again
                try:
                    # take the '/' out so you have two intgers side by side
                    type_move = type_move.split('/')
                    # sets the first integer as stool one
                    stool_1 = int(type_move[0])
                    # set the second inetger as stool two
                    stool_2 = int(type_move[1])
                    # will use the move function to move the cheese
                    move(self._game, stool_1, stool_2)
                    # if the game looks like the solution
                    if self._game == self._finshed_game:
                        # prints the solution of the game
                        print(self._game)
                        # prints conratulation for completing the game
                        print("Mr.Debugger: Well... YOU WIN! CONGRATULATION!")
                # if any error occurs it will say try again
                except:
                    print("TRY AGAIN! INVALID!!!")
        # this will  show up once they quit or finish the game
        print("Thanks for playing")

if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.
    print('''
        WELCOME!
        Here to play I see:
        To start: please enter an integer for number of cheese.
        After that an integer for number of stools.
        -Number of cheese must be greater than or equal to 1
        -Number of stools must be greater than or equal to 3
        After done! Please read instructions and rules!
        ''')
    # holds input for the number of cheese
    num_cheese = ''
    # holds input for the number of stools
    num_stool = ''
    # this will make sure the cheese first
    # if the cheese input is an int and if its greater or equal to 1 to be
    # valid cheese number
    while type(num_cheese) != int or int(num_cheese) <= 0:
        # it will try to make sure the input is valid and if it
        # isnt then cause error
        try:
            # asks for the input for how many cheese is wanted
            num_cheese = input('Number of cheeses: ')
            # turns input into an int
            num_cheese = int(num_cheese)
            # number of cheese is not less then or equal to 0
            if num_cheese <= 0:
                # error message
                print('Enter proper integer bigger than or equal to 1')
        # if conditions arent met enters error message
        except:
            print('Enter proper integer bigger than or equal to 1')
    # will make sure for stool second same thing like cheese
    # it will check if the it is an int and greater equal to 3
    while type(num_stool) != int or int(num_stool) <= 2:
        # it will try and if condition are not met it will ask the player
        # to try this again
        try:
            # takes the input for the number of stools the person wants
            num_stool = input('Number of stools: ')
            # changes the string into an int
            num_stool = int(num_stool)
            # makes sure if the stool isnt smaller than 3
            if num_stool <= 2:
                print('Enter proper integer bigger than or equal to 3')
        # any errors it will say to enter proper integer
        except:
            print('Enter proper integer bigger than or equal to 3')
    # this will create the game by using the variable we obtain
    create_game = ConsoleController(num_cheese, num_stool)
    # prints layout of the game
    print(create_game._game)
    # starts the game
    create_game.play_loop()
