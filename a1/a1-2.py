class MatrixIndexError(Exception):
    '''An attempt has been made to access an invalid index in this matrix'''


class MatrixDimensionError(Exception):
    '''An attempt has been made to perform an operation on this matrix which
    is not valid given its dimensions'''


class MatrixInvalidOperationError(Exception):
    '''An attempt was made to perform an operation on this matrix which is
    not valid given its type'''


class MatrixNode():
    '''A general node class for a matrix'''

    def __init__(self, contents, right=None, down=None):
        '''(MatrixNode, obj, MatrixNode, MatrixNode) -> NoneType
        Create a new node holding contents, that is linked to right
        and down in a matrix
        '''
        self._contents = contents
        self._right = right
        self._down = down

    def __str__(self):
        '''(MatrixNode) -> str
        Return the string representation of this node
        '''
        return str(self._contents)

    def get_contents(self):
        '''(MatrixNode) -> obj
        Return the contents of this node
        '''
        return self._contents

    def set_contents(self, new_contents):
        '''(MatrixNode, obj) -> NoneType
        Set the contents of this node to new_contents
        '''
        self._contents = new_contents

    def get_right(self):
        '''(MatrixNode) -> MatrixNode
        Return the node to the right of this one
        '''
        return self._right

    def set_right(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set the new_node to be to the right of this one in the matrix
        '''
        self._right = new_node

    def get_down(self):
        '''(MatrixNode) -> MatrixNode
        Return the node below this one
        '''
        return self._down

    def set_down(self, new_node):
        '''(MatrixNode, MatrixNode) -> NoneType
        Set new_node to be below this one in the matrix
        '''
        self._down = new_node


class Matrix():
    '''A class to represent a mathematical matrix
    Note: Uses 0-indexing, so an m x n matrix will have
    indices (0,0) through (m-1, n-1)'''

    def __init__(self, m, n, default=0):
        '''(Matrix, int, int, float) -> NoneType
        Create a new m x n matrix with all values set to default
        '''
        # Repersentation Invarient
        # head is the very top left of the matrix frame
        # head is an Matrix Node
        # row is # of rows in the Matrix(int)
        # col is # of cols in the Matrix(int)
        # Head is the corner that leads the frame of matrix
        # which is built with matrix Nodes starting at head
        # then works all the way to # of cols - 1 and
        # the # of rows -1
        # Then the actual dimensions and matrix is built inside
        # the frame with Matrix nodes using the dimensions row and col
        # and puting 0 if not # was put in parameter of every matrixNode
        # made
        self._head = MatrixNode(None)
        self._row = m
        self._col = n
        # count variables to track the correct number of row and col
        count_row = 1
        count_col = 1
        # with dimensions of 0 there is no matrix
        if m == 0 or n == 0:
            raise MatrixDimensionError
        else:
            # creates the frame of the matrix
            # First assign bot bottom and right from head 0
            self._head._down = MatrixNode(0)
            self._head._right = MatrixNode(0)
            # having pointer to know which Node is being assigned
            pointer1 = self._head._down
            pointer2 = self._head._right
            # This will assign the column frame
            while not(count_col == n):
                pointer1._down = MatrixNode(count_col)
                pointer1 = pointer1._down
                count_col += 1
            # This will assign the row Frame
            while not(count_row == m):
                pointer2._right = MatrixNode(count_row)
                pointer2 = pointer2._right
                count_row += 1
            # count variables for the actual value matrix inside frame
            count_inner_row = 0
            # pointer to keep track of the matrix
            pointer1 = self._head._down
            # creates the inner matrix with default value
            while not(count_inner_row == m):
                new_pointer1 = pointer1
                count_inner_col = 0
                while not(count_inner_col == n):
                    # creates the columns first
                    new_pointer1._right = MatrixNode(default)
                    new_pointer1 = new_pointer1._right
                    count_inner_col += 1
                # then moves on to next row
                pointer1 = pointer1._down
                count_inner_row += 1
            # makes sure all columns are connected to node under
            pointer1 = self._head
            pointer2 = self._head._down
            for y in range(self._row - 1):
                new_pointer1 = pointer1
                new_pointer2 = pointer2
                for x in range(self._col - 1):
                    new_pointer1._right._down = new_pointer2._right
                    new_pointer1 = new_pointer1._right
                    new_pointer2 = new_pointer2._right
                pointer1 = pointer1._down
                pointer2 = pointer1._down

    def get_val(self, i, j):
        '''(Matrix, int, int) -> float
        Return the value of m[i,j] for this matrix m
        '''
        # count variable to count number of cols till it gets there
        count = 0
        # pointer to point to the first row
        pointer1 = self._head
        # makes sure if dimension row is valid
        if 0 < i <= self._row:
            # makes sure if dimension col is valid
            if 0 < j <= self._col:
                # reaches the column
                while not(count == i):
                    pointer1 = pointer1._down
                    count += 1
                # new count for row
                count_down = 0
                # goes down till reaches row
                while not(count_down == j):
                    pointer1 = pointer1._right
                    count_down += 1
                # returns the contents of the node wanted
                return(pointer1._contents)
            else:
                raise MatrixIndexError
        else:
            raise MatrixIndexError

    def set_val(self, i, j, new_val):
        '''(Matrix, int, int, float) -> NoneType
        Set the value of m[i,j] to new_val for this matrix m
        '''
        # count variable to count number of cols
        count = 0
        # pointer to point to first row
        pointer1 = self._head
        # if dimensions rows is valid
        if 0 < i <= self._row:
            # if dimensions columns is valid
            if 0 < j <= self._col:
                # goes to the column wanted
                while not(count == i):
                    pointer1 = pointer1._down
                    count += 1
                # resets counter for rows
                count_down = 0
                # goes to the row wanted
                while not(count_down == j):
                    pointer1 = pointer1._right
                    count_down += 1
                # changes node into new data
                pointer1._contents = new_val
            else:
                raise MatrixIndexError
        else:
            raise MatrixIndexError

    def get_row(self, row_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the row_num'th row of this matrix
        '''
        # makes sure row chosen is valid in matrix
        if 0 < row_num <= self._row:
            # count variable to count to that row
            count = 1
            # pointer pointing on first row
            pointer1 = self._head._down
            # goes to chosen row
            while not(count == row_num):
                pointer1 = self._head._down
                count += 1
            # pointer point s to beginnging of row
            pointer1 = pointer1._right
            # creates thr row matrix
            the_row = OneDimensionalMatrix(1, self._col)
            # points to the start of row matrix
            pointer_row = the_row._head._down
            # adds all contents of the orginal matrix into one dimensional
            for x in range(self._col - 1):
                pointer_row._right._contents = pointer1._contents
                pointer_row = pointer_row._right
                pointer1 = pointer1._right
            # returns the row
            return(the_row)
        else:
            # if doesnt follow conditions
            raise MatrixIndexError

    def set_row(self, row_num, new_row):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the row_num'th row of this matrix to those of new_row
        '''
        # makes sure if dimensions are correct for new row
        if not(new_row._col == self._col):
            raise MatrixDimensionError
        # makes sure if row num is in fact in the proper dimension
        elif 0 < row_num <= self._row:
            # count variable to hold how many time iterated
            count = 1
            # points to first row
            pointer1 = self._head._down
            # goes to the correct row
            while not(count == row_num):
                pointer1 = pointer1._down
                count += 1
            # point to first value of matrix
            pointer1 = pointer1._right
            # points to first value of row matrix
            curr = new_row._head._down._right
            # adds value from new_row to the old row
            for x in range(self._col - 1):
                pointer1._contents = curr._contents
                pointer1 = pointer1._right
                curr = curr._right
        else:
            # if conditions are not met
            raise MatrixIndexError

    def get_col(self, col_num):
        '''(Matrix, int) -> OneDimensionalMatrix
        Return the col_num'th column of this matrix
        '''
        # if col number given is valid
        if 0 < col_num <= self._col:
            # count variable to hold
            count = 1
            # pointer pointing at first column
            pointer1 = self._head._right
            # moves to correct column
            while count != col_num:
                pointer1 = pointer1._right
                count += 1
            # goes down to first value fo column
            pointer1 = pointer1._down
            # creates a onedimensionMatrix
            the_col = OneDimensionalMatrix(self._row, 1)
            # pointer pointing at start of one dimensional matrix
            pointer_col = the_col._head._right
            # adds evey element of column into one dimensional matrix
            for x in range(self._row - 1):
                pointer_col._down._contents = pointer1._contents
                pointer_col = pointer_col._down
                pointer1 = pointer1._down
            # returns the column asked for
            return(the_col)
        else:
            # if conditions are not met
            raise MatrixIndexError

    def set_col(self, col_num, new_col):
        '''(Matrix, int, OneDimensionalMatrix) -> NoneType
        Set the value of the col_num'th column of this matrix to those of
        new_row
        '''
        # this will check if col in dimension
        if 0 < col_num <= self._col:
            # counts the numbe rof cols
            count = 1
            # pointer at first col
            pointer1 = self.head._right
            # goes to the correct column
            while count != col_num:
                pointer1 = self.head._right
                count += 1
            # goes to start of martix col
            pointer1 = pointer1._down
            # goes the column given start
            curr = new_col._head._down._right
            # add contents of column into wanted column
            for x in range(self._row - 1):
                pointer1._contents = curr._contents
                pointer1 = pointer1._down
                curr = curr._down
        else:
            # if conditions havent met
            raise MatrixIndexError

    def swap_rows(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of rows i and j in this matrix
        '''
        # Checks is rows are in range of dimensions
        if (i > self._row) or (j > self._row):
            raise MatrixIndexError
        # if rows are negetaive or dimension 0
        elif (i <= 0) or (j <= 0):
            raise MatrixIndexError
        else:
            # gets the two rows using get_row
            row_i = self.get_row(i)
            row_j = self.get_row(j)
            # set the rows with set_row
            self.set_row(i, row_j)
            self.set_row(j, row_i)

    def swap_cols(self, i, j):
        '''(Matrix, int, int) -> NoneType
        Swap the values of columns i and j in this matrix
        '''
        # the columns are in ranges of dimensions
        if (i._col > self._col) or (j._col > self._col):
            raise MatrixIndexError
        # if dimensions are less or 0
        elif (i._col <= 0) or (j._col <= 0):
            raise MatrixIndexError
        else:
            # gets both columns using get_columns
            colum_i = self.get_col(i)
            colum_j = self.get_col(j)
            # set the columns using set_col
            self.set_col(i, colum_j)
            self.set_col(j, colum_i)

    def add_scalar(self, add_value):
        '''(Matrix, float) -> NoneType
        Increase all values in this matrix by add_value
        '''
        # points to the first columns
        pointer = self._head._right
        # count to hold the number of time to the right
        count_col = 1
        # adds the values to the first columns then in the element
        # the entire row and loops through entire matrix
        while not(count_col == self._col):
            pointer._down._contents += add_value
            count_col += 1
            count_row = 1
            new_point = pointer
            # goes through the row of that column element
            while not(count_row == self._row):
                new_point._right._contents += add_value
                new_point = new_point._right
                count_row += 1
            # goes to the next part of column
            pointer = pointer._down

    def subtract_scalar(self, sub_value):
        '''(Matrix, float) -> NoneType
        Decrease all values in this matrix by sub_value
        '''
        # pointer points to the first column
        pointer = self._head._right
        # checks the column its at with a count
        count_col = 1
        # goes through the column and in the part of the column the entire
        # row to subtract
        while not(count_col == self._col):
            pointer._down._contents -= sub_value
            count_col += 1
            count_row = 1
            new_point = pointer
            # goes the entire row to subtract in the matrix
            while not(count_row == self._row):
                new_point._right._contents -= sub_value
                new_point = new_point._right
                count_row += 1
            # goes to the next part of the column
            pointer = pointer._down

    def multiply_scalar(self, mult_value):
        '''(Matrix, float) -> NoneType
        Multiply all values in this matrix by mult_value
        '''
        # points to the first part of the column
        pointer = self._head._right
        # count variable to count the columns
        count_col = 1
        # goes through columns and each part of the first column the entire
        # row is multiplied with scalar
        while not(count_col == self._col):
            hold = pointer._down._contents
            hold = hold * mult_value
            count_col += 1
            count_row = 1
            new_po = pointer
            # goes through the entire row and multiplies it
            while not(count_row == self._row):
                hold = new_po._right._contents
                hold = hold * mult_value
                new_po = new_po._right
                count_row += 1
            # goes to next part of column
            pointer = pointer._down

    def add_matrix(self, adder_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the sum of this matrix and adder_matrix
        '''
        # check is it has apporiate columns
        if not(self._col == adder_matrix._col):
            raise MatrixDimensionsError
        # checks if it has apporiate rows
        elif not(self._row == adder_matrix._row):
            raise MatrixDimensionError
        else:
            # pointer to point at both matrix heads
            point1 = self._head
            point2 = adder_matrix._head
            # new return matrix thats empty
            ret_matrix = Matrix(self._row, self._col)
            # pointer at the matrix head
            point3 = ret_matrix._head
            # goes down the matrix until its at the end
            while not(point1._down is None):
                # pointers for all three matrices
                point1 = point1._down
                col_point1 = point1
                point2 = point2._down
                col_point2 = point2
                point3 = point3._down
                col_point3 = point3
                # at those pointers they add into the empty matrix for each
                # part of the row then goes to next row
                while not(col_point1._right is None):
                    col_point3._right._contents = col_point1._right._contents
                    col_point3._right._contents += col_point1._right._contents
            # return the final matrix
            return(ret_matrix)

    def multiply_matrix(self, mult_matrix):
        '''(Matrix, Matrix) -> Matrix
        Return a new matrix that is the product of this matrix and mult_matrix
        '''
        if not(self._col == mult_matrix._row):
            raise MatrixDImensionError
        else:
            pass


class OneDimensionalMatrix(Matrix):
    '''A 1xn or nx1 matrix.
    (For the purposes of multiplication, we assume it's 1xn)'''

    def get_item(self, i):
        '''(OneDimensionalMatrix, int) -> float
        Return the i'th item in this matrix
        '''
        # if columns dimension is greater
        if i > self._col:
            raise MatrixIndexError
        # if columns dimension i snegative or 0
        elif i <= 0:
            raise MatrixIndexError
        else:
            # if its horizontal
            if self._col > 1:
                # goes down to the row
                point = self._head._down
                for x in range(i - 1):
                    point = point._right
                y = point._contents
            # if its vertical
            elif self._row > 1:
                # goes down column
                point = self._head._right
                for x in range(i - 1):
                    point = point._down
                y = point._contents
            return(x)

    def set_item(self, i, new_val):
        '''(OneDimensionalMatrix, int, float) -> NoneType
        Set the i'th item in this matrix to new_val
        '''
        # check if it meet dimensions
        if i > self._col:
            raise MatrixIndexError
        # check if negative or 0
        elif i <= 0:
            raise MatrixIndexError
        else:
            # if its horizontal
            if self._col > 1:
                # goes down the row
                point = self._head._down
                for x in range(i - 1):
                    point = point._right
                point._contents = new_val
            # if its vertical
            else:
                # goes down the column
                point = self._head._right
                for x in range(i - 1):
                    point = point._down
                point._contents = new_val


class SquareMatrix(Matrix):
    '''A matrix where the number of rows and columns are equal'''

    def transpose(self):
        '''(SquareMatrix) -> NoneType
        Transpose this matrix
        '''
        pass

    def get_diagonal(self):
        '''(Squarematrix) -> OneDimensionalMatrix
        Return a one dimensional matrix with the values of the diagonal
        of this matrix
        '''
        # pointer at the beginnning of matrix
        pointer = self._head
        # gets an empty matrix
        diagonal = OneDimensionalMatrix(1, self._col)
        # points to start of matrix
        diagonal_point = diagonal._head._down
        # places each diagonal element in empty matrix
        for x in range(self._col - 1):
            pointer = pointer._down._right
            diagonal_point._right._contents = pointer._contents
            diagonal_point = diagonal_point._right
        # returns matrix
        return(diagonal)

    def set_diagonal(self, new_diagonal):
        '''(SquareMatrix, OneDimensionalMatrix) -> NoneType
        Set the values of the diagonal of this matrix to those of new_diagonal
        '''
        # points to the head of the matrix
        pointer = self._head
        # if the given matrix doesnt fit
        if not(new_diagonal._col == self._col):
            raise MatrixDimensionError
        else:
            # points the first diagonal point
            diagonal_point = new_diagonal._head._down
            # goes through to place all diagonal into the matrix
            for x in range(self._col - 1):
                pointer = pointer._down._right
                pointer = diagonal_point._right._contents
                diagonal_point = diagonal_point._right


class SymmetricMatrix(SquareMatrix):
    '''A Symmetric Matrix, where m[i, j] = m[j, i] for all i and j'''


class DiagonalMatrix(SquareMatrix, OneDimensionalMatrix):
    '''A square matrix with 0 values everywhere but the diagonal'''


class IdentityMatrix(DiagonalMatrix):
    '''A matrix with 1s on the diagonal and 0s everywhere else'''