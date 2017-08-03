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
Harri Pahirathan
Assignment 2
2017-07-31
ENJOY!
"""
from ConsoleController import ConsoleController
from GUIController import GUIController
from TOAHModel import TOAHModel

import time
NUM_CHEESES = 3


def tour_of_four_stools(model: TOAHModel, delay_btw_moves: float=0.5,
                        console_animate: bool=False):
    """Move a tower of cheeses from the first stool in model to the fourth.
       model - a TOAHModel with a tower of cheese on the first stool
                and three other empty stools
       console_animate - whether to use ConsoleController to animate the tour
       delay_btw_moves - time delay between moves in seconds IF
                         console_animate == True
                         no effect if console_animate == False
    """
    # this will get the total number of cheeses in the model
    total_cheese = model.number_of_cheeses()
    # animate is set to false unless asked for will become true later on
    animate = False
    # represntation for stool 1
    stool1 = 0
    # represntation for stool 2
    stool2 = 1
    # represntation for stool 3
    stool3 = 2
    # represntation for stool 4
    stool4 = 3
    # if its wanted to be animated
    if console_animate is True:
        # now the models will appear
        animate = True
        # it creates(prints) model in the sheel
        print(model)
        # adds the time delay
        time.sleep(delay_btw_moves)
        # calls the helper function in which it will recursilely
        # do the optimal number of moves to complete the model
        four_stool(model, total_cheese, stool1, stool2, stool3, stool4,
                   animate,
                   delay_btw_moves)
    else:
        # calls the helper function that will take four stools to check
        # how many moves it takes using the equation
        four_stool(model, total_cheese, stool1, stool2, stool3, stool4,
                   animate,
                   delay_btw_moves)


def four_stool(model, num_cheeses, stool1, stool2, stool3, stool4, animate,
               delay_btw_moves):
    '''
    Helper function
    This will use the equation and moves the cheeses and get the total
    moves that it takes and the moves it takes should be the optimal
    number of moves it takes
    '''
    # this equations holds for the efficent way of getting number moves
    # for 4 of stools, therefore used to find for any number of cheese
    # this equation is used to find new_num_of_cheeses in which has worked
    # for 1-10 cheeses which I believe is efficent in finding the efficent
    # number of moves
    # this equation was the ideal one to use as this one worked after
    # breaking it down in TOAH and doing many skteches, it was the formula
    # for i in which new is the number of cheese for four stool
    equation = 2*num_cheeses
    equation = equation + (1/4)
    equation = round((equation**(1/2))-(1/2))
    equation = num_cheeses - equation
    # takes the total number of cheeses and subtract it with the equation
    new_num = num_cheeses - equation
    # once i recursivly calls itself then it uses three stools
    # to calculate the number of moves
    # base case of 1 cheese or 2 it just uses the three stool hanoi helper
    if num_cheeses == 1 or num_cheeses == 2:
        # calls the three stool helper function
        three_stool(model, num_cheeses, stool1, stool2, stool4, animate,
                    delay_btw_moves)
    else:
        # uses four stools but rotates the last stool with the 2nd stool
        # uses the equations cheese to random spot for now
        four_stool(model, equation, stool1, stool4, stool3, stool2, animate,
                   delay_btw_moves)
        # uses the three stool parameter with first, third, fourth
        # uses the new cheese remaining into the final stool
        three_stool(model, new_num, stool1, stool3, stool4, animate,
                    delay_btw_moves)
        # this uses four stools and roatest first stool with second stool
        # also using the equations cheese to the final stool
        four_stool(model, equation, stool2, stool1, stool3, stool4, animate,
                   delay_btw_moves)


def three_stool(model, new, stool1, stool2, stool3, animate, delay_btw_moves):
    '''
    helper function
    Does tower of hanoi and moves everything in three stools
    using base case and rearranging.
    '''
    # takes in 1 cheese after recursvivly calling itself and
    # moves the cheese from first to second
    # base case of one cheese juust move to end
    if new == 1:
        # moves the cheese from the beginning the first to final end stool
        model.move(stool1, stool3)
        # if animation was asked it would run if statement since a
        # move has occured
        if animate is True:
            # printing the model
            print(model)
            # putting the time delay
            time.sleep(delay_btw_moves)
    else:
        # calls itself again but reorders to stool and move cheese -l
        # to random spot for now
        three_stool(model, new-1, stool1, stool3, stool2, animate,
                    delay_btw_moves)
        # moves the cheese from first to final end stool
        model.move(stool1, stool3)
        # if animation was asked it would run if statement since a
        # move has occured
        if animate is True:
            # prints out model
            print(model)
            # adds time delay after model has been printed
            time.sleep(delay_btw_moves)
        # calls itself again but get the cheese -1 to final end stool
        three_stool(model, new-1, stool2, stool1, stool3, animate,
                    delay_btw_moves)

if __name__ == '__main__':
    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(number_of_cheeses=8)
    tour_of_four_stools(four_stools,
                        console_animate=False,
                        delay_btw_moves=0.5)
    print(four_stools.number_of_moves())
