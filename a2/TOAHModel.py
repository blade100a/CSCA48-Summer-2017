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
TOAHModel:  Model a game of Towers of Anne Hoy
Cheese:   Model a cheese with a given (relative) size
IllegalMoveError: Type of exceptions thrown when an illegal move is attempted
MoveSequence: Record of a sequence of (not necessarily legal) moves. You will
need to return MoveSequence object after solving an instance of the 4-stool
Towers of Anne Hoy game, and we will use that to check the correctness of your
algorithm.
"""
"""
Harri Pahirathan
Assignment 2
2017-07-31
ENJOY!
"""


class TOAHModel:
    """Model a game of Towers Of Anne Hoy.

    Model stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.  Note that
    large, aged, cheeses at the bottom of each pile serve as stools, and
    these may not be moved!

    fill_first_stool - put an existing model in the standard starting config
    move - move cheese from one stool to another
    add - add a cheese to a stool
    cheese_location - index of the stool that the given cheese is on
    number_of_cheeses - number of cheeses in this game
    number_of_moves - number of moves so far
    number_of_stools - number of stools in this game
    get_move_seq - MoveSequence object that records the moves used so far
    """
    def __init__(self, total_stools):
        '''
        container: Nested List
        Takes a integer and for that integer creates that many nested list
        which represents the number of stools. Also holds then number of
        moves.
        '''
        # Representation Invarient
        # stools is the container in which will hold both stools and cheese
        # stool has nested list repsenting stools
        # stools nested list has cheese ordedr biggest -> smallest
        # moves records all moves performed in the model
        # cheese will be taken out from the back of the nested list
        # as it repersents the top of the stool
        # this is the container that holds the entire  nested list
        self._stools = []
        # this will create a nested list for the number of stools
        # wanted to be made
        for x in range(total_stools):
            # adds a list into the list
            self._stools.append([])
        # this will hold the number of moves made by calling the move
        # sequence
        self._moves = MoveSequence([])

    def fill_first_stool(self: 'TOAHModel', number_of_cheeses: int):
        '''
        Put number_of_cheeses cheeses on the first (i.e. 0-th) stool, in order
        of size, with a cheese of size == number_of_cheeses on bottom and
        a cheese of size == 1 on top.
        '''
        # creates a copy for the number of cheeses wanted
        x = number_of_cheeses
        # this will then loop through until no more cheeses are needed
        # to be added and the biggest cheese will be infront representing
        # the botttom of the stack, while smallest cheese on the back
        # representing the top of the stack
        while x != 0:
            # adds the cheese from largest -> smallest
            self._stools[0].append(Cheese(x))
            # descreses the total as it will loop until no more cheese are
            # needed to be added
            x = x - 1

    def move(self, stool1, stool2):
        '''
        Takes two integers and using the first integer to take the cheese from
        that stool and move it to the second integer stool. Of course if its
        a bigger cheese to smaller one, it wont execute
        '''
        # this represents the frist stool
        x = self._stools[stool1]
        # this represents the second_stool
        y = self._stools[stool2]
        # the it will check if the stool is empty it can go on
        if y == []:
            # moves cheese from first stool to second
            y.append(x[-1])
            # deletes cheese from the previous stool
            x.pop()
            # adds the move perfromed to move sequence
            self._moves.add_move(stool1, stool2)
        # checks if the cheese from  curr stool is smaller
        elif x[-1].size <= y[-1].size:
            # moves cheese from first stool to second
            y.append(x[-1])
            # deletes cheese from the previous stool
            x.pop()
            # adds the move perfromed to move sequence
            self._moves.add_move(stool1, stool2)
        # if conditions arent meant then its an Illegeal move which will
        # raise the error
        else:
            raise IllegalMoveError

    def add(self, stool_index, cheese):
        '''
        Takes the stool wanted and cheese, and it will add the cheese to the
        stool. But it will check if its empty or cheese is smaller then top
        cheese on stool.
        '''
        # gets the size of the cheese
        size1 = cheese.size
        # if the stool wanted to add is empty then it'll just add the cheese
        if self._stools[stool_index] == []:
            # gets stool from  the container
            x = self._stools[stool_index]
            # adds the cheese into stool
            x.append(cheese)
        # if the cheese is smaller then the cheese on the stool
        elif size1 < self._stools[stool_index][-1].size:
            # gets stool from  the container
            x = self._stools[stool_index]
            # adds the cheese into stool
            x.append(cheese)
        # if conditions arent met then its an Illegal move
        # raises the error
        else:
            raise IllegalMoveError

    def cheese_location(self, wanted_cheese):
        '''
        Has a cheese and looks through every stool to see if any cheese is
        the same. But if there is no cheese then its going to return
        None.
        '''
        # creates and sets position variable as None
        position = None
        # loops through the container to see every stool in the
        # container
        for x in range(len(self._stools)):
            # holds all the stools
            every_stool = self._stools[x]
            # checks if the cheese is in the stool
            if wanted_cheese in every_stool:
                # assigns position with the stool the cheese is at
                position = x
        # returns the position of the cheese if found
        return(position)

    def number_of_cheeses(self):
        '''
        This will go through every stool and counts how many
        cheese are currently in the container and return a int
        '''
        # count variable
        count = 0
        # loops through position of stool
        for x in self._stools:
            # takes the length of the stool
            x = len(x)
            # then adds the len of the stool into the count variable
            count += x
        # returns the total number of cheese
        return(count)

    def number_of_stools(self):
        '''
        This will go through the container and count the number
        of nested list which represents the number of stools. Returns
        an int at the end.
        '''
        # count variable
        count = 0
        # loops through nested list and adds one to count
        for x in self._stools:
            # adds 1 to the count variable for every stool
            count = count + 1
        # returns the total number of nested lists
        return(count)

    def _cheese_at(self: 'TOAHModel', stool_index,
                   stool_height: int) -> 'Cheese':
        """
        If there are at least stool_height+1 cheeses
        on stool stool_index then return the (stool_height)-th one.
        Otherwise return None.

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M._cheese_at(0,3).size
        2
        >>> M._cheese_at(0,0).size
        5
        """
        # gets the length of the stool asked
        index_stool = len(self._stools[stool_index])
        height = stool_height + 1
        # checks the height is less then the len of stool or equal too
        if (height) <= index_stool:
            # finds the stool and the cheese at the wanted height
            x = self._stools[stool_index][stool_height]
        # if condition aren tmet then no cheese exists
        else:
            # so it will return none
            x = None
        # returns the cheese if exisits
        return(x)

    def top_cheese(self, stool_index):
        '''
        Finds the cheese on wnated stool and returns the top cheese in that
        stool.
        '''
        # gets the top cheese form index
        top_cheese = self._stools[stool_index][-1]
        # returns the cheese
        return(top_cheese)

    def number_of_moves(self):
        '''
        checks the number of moves made in the game by calling the variable
        move from init.
        '''
        # reutnrs the total number of move form move sequence
        return(self._moves.length())

    def get_move_seq(self: 'TOAHModel') -> 'MoveSequence':
        # gets the variable in the init
        return self._move_seq

    def __eq__(self: 'TOAHModel', other: 'TOAHModel') -> bool:
        """
        We're saying two TOAHModels are equivalent if their current
        configurations of cheeses on stools look the same.
        More precisely, for all h,s, the h-th cheese on the s-th
        stool of self should be equivalent the h-th cheese on the s-th
        stool of other
        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0,1)
        >>> m1.move(0,2)
        >>> m1.move(1,2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0,3)
        >>> m2.move(0,2)
        >>> m2.move(3,2)
        >>> m1 == m2
        True
        """
        # checks if stool is equal to number of other
        if self._stools == other._stools:
            # result is true so returns true
            result = True
        # models arent the same therefore
        else:
            # retruns false
            result = False
        # returns result which is bool
        return(result)

    def __str__(self: 'TOAHModel') -> str:
        """
        Depicts only the current state of the stools and cheese.
        """
        stool_str = "=" * (2 * (self.number_of_cheeses()) + 1)
        stool_spacing = "  "
        stools_str = (stool_str + stool_spacing) * self.number_of_stools()

        def cheese_str(size: int):
            if size == 0:
                return " " * len(stool_str)
            cheese_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(stool_str) - len(cheese_part)) / 2)
            return space_filler + cheese_part + space_filler

        lines = ""
        for height in range(self.number_of_cheeses() - 1, -1, -1):
            line = ""
            for stool in range(self.number_of_stools()):
                c = self._cheese_at(stool, height)
                if isinstance(c, Cheese):
                    s = cheese_str(int(c.size))
                else:
                    s = cheese_str(0)
                line += s + stool_spacing
            lines += line + "\n"
        lines += stools_str
        return lines


class Cheese:
    def __init__(self: 'Cheese', size: int):
        """
        Initialize a Cheese to diameter size.

        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """
        self.size = size

    def __repr__(self: 'Cheese') -> str:
        """
        Representation of this Cheese
        """
        return "Cheese(" + str(self.size) + ")"

    def __eq__(self: 'Cheese', other: 'Cheese') -> bool:
        """Is self equivalent to other? We say they are if they're the same
        size."""
        return isinstance(other, Cheese) and self.size == other.size


class IllegalMoveError(Exception):
    pass


class MoveSequence(object):
    def __init__(self: 'MoveSequence', moves: list):
        # moves - a list of integer pairs, e.g. [(0,1),(0,2),(1,2)]
        self._moves = moves

    def get_move(self: 'MoveSequence', i: int):
        # Exception if not (0 <= i < self.length)
        return self._moves[i]

    def add_move(self: 'MoveSequence', src_stool: int, dest_stool: int):
        self._moves.append((src_stool, dest_stool))

    def length(self: 'MoveSequence') -> int:
        return len(self._moves)

    def generate_TOAHModel(self: 'MoveSequence', number_of_stools: int,
                           number_of_cheeses: int) -> 'TOAHModel':
        """
        An alternate constructor for a TOAHModel. Takes the two parameters for
        the game (number_of_cheeses, number_of_stools), initializes the game
        in the standard way with TOAHModel.fill_first_stool(number_of_cheeses),
        and then applies each of the moves in move_seq.
        """
        model = TOAHModel(number_of_stools)
        model.fill_first_stool(number_of_cheeses)
        for move in self._moves:
            model.move(move[0], move[1])
        return model

    def __repr__(self: 'MoveSequence') -> str:
        return "MoveSequence(" + repr(self._moves) + ")"


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
