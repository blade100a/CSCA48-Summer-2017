class InvalidDimension(Exception):
    '''
    This will stop when inproper use of dimension occurs
    '''
    pass

class InvalidType(Exception):
    '''
    This will stop them from suing improper type varibles like subtracting
    strings
    '''
    pass

class Matrix():
    ''' An ADT that will deal with types of Matricies using a list'''
    
    def __init__(self, marix_list):
        '''(Matrix) -> NoneType
        Creates a list of the matrix that will deal with in
        the ADT. Number of list inside represents number of
        rows and the elements inside those represent columns.
        REQ: must have proper format[[]]
        REQ: outer list holds number of rows
        REQ: inner lists holds elements rep number of columns
        '''
        pass

    def num_columns(self):
        '''(Matrix) -> int
        This will take the first part of the list then
        counts every element of that list part taken out,
        which represents the number of columns. This will be
        the dimension and cant be changed.
        '''
        pass
    
    def num_rows(self):
        '''(Matrix) -> int
        This will count every element of the list, which
        represents the number of rows in the matrix. This will be
        the number of rows and cant be changed.
        '''
        pass
    
    def add_matrix(self, matrix_2):
        '''(Matrix, Matrix) -> NoneType
        This will get the num of rows and columns of both matrix to make
        sure that both have same dimensions. Then if its true, it will
        get every value seperately and add into two seperate list for both
        matrcies. It will then check whether its a string or a int then it 
        will add the same position elements of each list depending on type
        together into one list. Then sets the variables back in the same
        dimensions original. If False for different dimensions it will
        tell raise invaliddimension exception.
        '''
        pass
    
    def subtract_matrix(self, matrix_2):
        '''(Matrix, Matrix) -> NoneType
        This will get the num of rows and columns of both matrix to make
        sure that both have same dimensions. Then if its true, it will
        get every value seperately and add into two seperate list for both
        matrcies. The it will subtract the same position elements of each list
        together into one list. Then sets the variables back in the same
        dimensions original. If False for different dimensions it will tell
        raise invaliddimension exception. If element is string then raise 
        Invalid Type.
        REQ: int matrix
        REQ: Same dimensions
        '''
        pass
    
    def multiply_matrix(self, matrix_2):
        '''(Matrix, Matrix) -> NoneType
        This will make sure if the columns of matrix 1 is the same
        as the rows of matrix 2. The you can multiply but if not 
        you cant and raise Invalid Dimension Exception. If type is
        string raise Invalid Type.
        REQ: int Matrix
        REQ: same Dimensions
        '''
        pass
    
    def get_value(self, row1, column1):
        '''(Matrix, int, int) -> int or str
        This will check if the row and column are in the range of the
        dimensions of the matrix. If true, then finds variable in given
        of the row and column given.
        '''
        pass
    
    def set_value(self, obj, row1, column1):
        '''(Matrix, int or str, int, int) -> Nonetype
        This will check if the row and column are in the range of the
        dimensions of the matrix. If true, then finds the position
        of the column and row and place obj in that part of the matrix.
        '''
        pass
    
    def swap_row(self, row1, row2):
        '''(Matrix, int, int) -> NoneType
        This will make sure if the rows asked are in the matrix using num_rows.
        Then if true, it will find position of the rows in the list and save
        them into different variables then replace the rows with the other row.
        Vice versa.
        '''
        pass
    
    def swap_column(self, column1, column2):
        '''(Matrix, int, int) -> NoneType
        This will make sure if the columns asked are in the matrix using num_
        columns. Then if true, it will get the position 
        '''
        pass
    
    def transpose_matrix(self):
        '''(Matrix) -> NoneType
        This will get the values in each row and switch the values into
        columns strating from the 1st row down to column.
        '''
        pass
    
    def get_row(self, row1):
        '''(Matrix, int) -> list
        This gets the row asked by going through the outer list getting
        the position of that row. Checks row position belongs in between
        dimensions before getting row.
        '''
        pass
    
    def set_row(self, obj_row, row1):
        '''(Matrix, list, int) -> NoneType
        This will find the row by going through the outer list and
        replace with new list with exact number of elements. Checks row
        position belongs in between dimensions between setting row.
        '''
        pass
    
    def get_column(self, column1):
        '''(Matrix, int) -> list
        This will get the column by geting the column in each inner list
        that is asked for into a new_list and return new list with those
        values or strings Checks column position belongs in between
        dimensions before getting column.
        '''
        pass
    
    def set_column(self, obj_column, column1):
        '''(Matrix, list, int) -> NoneType
        This will find the column need to replace going replace
        in each row which repersent the position of column.
        Checks column position belongs in between
        dimensions before setting column.
        '''
        pass
    
class OneDimensional(Matrix):
    
    def __init__(self, matrix_list):
        '''(Matrix(list)) -> NoneType
        Creates a list of the matrix that will deal with in
        the ADT. This will call parent class to create variable
        REQ: column or row must be 1 in dimensions
        '''
        pass
    
    def num_columns(self):
        '''(Matrix) -> int
        This will count each variable in the row by calling the num_columns
        in the parent class.
        '''
        pass
    
    def num_rows(self):
        '''(Matrix) -> int
        This will count each variable in the column list by calling the 
        num_rows in the parent class.
        '''
        pass    
    
    def add_matrix(self, matrix_2):
        '''(Matrix, Matrix) -> NoneType
        This will take another 1 dimensional matrix and call the add_matrix
        in the parent class.
        '''
        pass
    
    def subtract_matrix(self, matrix_2):
        '''(Matrix, Matrix) -> NoneType
        This will take another 1 dimensional matrix and call subtract_matrix
        in the parent class.
        '''
        pass
    
    def multiply_matrix(self, matrix_2):
        '''(Matrix, Matrix) -> NoneType
        This will check if the num of rows of the first matrix
        is the same
        '''
        pass
    
    def get_value(self, column1):
        '''(Matrix, int) -> int or str
        This will return the variable in the column of the 
        1 dimensional matrix.
        '''
        pass
    
    def set_value(self, obj, column1):
        '''(Matrix, int or str, int) -> NoneType
        This will replace the variable with another in the
        1 dimensional matrix.
        '''
        pass
    
    def transpose_matrix(self):
        '''(Matrix) -> NoneType
        This will make every element in the row into its own list which
        represent its own row. Representing the transpose 1dimensional
        matrix.
        '''
        pass
    
    def swap_column(self, column1, column2):
        '''(Matrix, int, int) -> NoneType
        This will get the 1 dimensional matrix row as one list, then find
        both columns and save those variables the replace them by using
        set_value function.
        '''
        pass
    
    def get_row(self, row1):
        '''(Matrix, int) -> list
        This will inheirt from the parent class so it can obtain the row
        asked
        '''
        pass
    
    def set_row(self, obj_row, row1):
        '''(Matrix, list, int) -> NoneType
        This will inheirt from the parent class so it can change a row into
        a different one
        '''
        pass
    
    def get_column(self, column1):
        '''(Matrix, int) -> list
        This will inheirt from the parent class so it can get a column from
        the matrix.
        '''
        pass
    
    def set_column(self, obj_column, column1):
        '''(Matrix, list, int) -> NoneType
        This will inheirt from the parent class so it can change a column into
        the column asked
        '''
        pass    
    
class SquareMatrix(Matrix):
    
    def __init__(self, matrix_list):
        '''(Matrix) -> NoneType
        Creates a list of the matrix that will deal with in
        the ADT. This will call parent class to create variable
        REQ: must be equal rows and columns
        '''
        pass
    def num_rows_and_columns(self):
        '''(Matrix) -> int
        This will count the num of rows by counting each element of the list
        then both rows and columns will represent that value.
        '''
        pass
    
    def add_matrix(self, matrix_2):
        '''(Matrix, Matrix) -> NoneType
        This will add the matrix by inheirting from the parent class
        add_matrix method.
        '''
        pass
    
    def subtract_matrix(self, matrix_2):
        '''(Matrix, Matrix) -> NoneType
        This will subtract the matrix by inheirting from the parent class
        subtract_matrix method.
        '''
        pass
    
    def multiply_matrix(self, matrix_2):
        '''(Matrix, Matrix) -> NoneType
        This will multiply the matrix by inheirting from the parent class
        multiply_matrix method.
        '''
        pass
    
    def get_value(self, row1, column1):
        '''(Matrix, int, int) -> int or str
        This will inheirt from the parent class get_value which will be able
        to obtain the int or str in the suggested row and column.
        '''
        pass
    
    def set_value(self, obj, row1, column1):
        '''(Matrix, int or str, int, int) -> NoneType
        This will inheirt from the parent class set_value which will be able
        to put the int or str in the suggested row and column.
        '''
        pass
    
    def transpose_matrix(self):
        '''(Matrix) -> NoneType
        This will inheirt from the parent class transpose_matrix which will
        be able to convert the rows into columns.
        '''
        pass
    
    def swap_column(self, column1, column2):
        '''(Matrix, int, int) -> NoneType
        This will inheirt from the parent class swap_column which will be able
        to switch the columns in the list with the other.
        '''
        pass
    
    def swap_row(self, row1, row2):
        '''(Matrix, int, int) -> NoneType
        This will inheirt from the parent class swap_row which will be able
        to switch the rows in the list with the other.
        '''
        pass
    
    def determinant_of_matrix(self):
        '''(Matrix) -> int
        This will make sure the dimensions of both columns and rows are
        2, If true, then it will proceed on take 1st of row1 and 2nds row2
        and multiply them. The take the 2nd of row1 and 1st row2 and multiply
        them. Then subtract the first multiplr wiht the second to get
        the determinant.
        '''
        pass
    
    def get_row(self, row1):
        '''(Matrix, int) -> list
        This will inheirt from the parent class so it can obtain the row
        asked
        '''
        pass
    
    def set_row(self, obj_row, row1):
        '''(Matrix, list, int) -> NoneType
        This will inheirt from the parent class so it can change a row into
        a different one
        '''
        pass
    
    def get_column(self, column1):
        '''(Matrix, int) -> list
        This will inheirt from the parent class so it can get a column from
        the matrix.
        '''
        pass
    
    def set_column(self, obj_column, column1):
        '''(Matrix, list, int) -> NoneType
        This will inheirt from the parent class so it can change a column into
        the column asked
        '''
        pass
    
    def set_diagonal(self, obj):
        '''(Matrix, int or str) -> NoneType
        This will get the dimensions of the square identity. Then it
        will get the range between the dimension and use parent class
        with set_value with (1,1), plus 1, till the dimension rep by n (n,n)
        of the obj that has the list needed for diagonal.
        '''
        pass
    
    def get_diagonal(self):
        '''(Matrix) -> list
        This will get the dimensions of the square identity. Then it
        will get the range between the dimension and use parent class
        with set_value with (1,1), plus 1, till the dimension rep by n (n,n)
        which will remove and place all elements into a list.
        '''
        pass

class Identity(SquareMatrix):
    
    def __init__(self, matrix_list):
        '''(Matrix) -> NoneType
        This will make a matrix which is represented as a list of 1s and 0s
        REQ: must be a valid identity
        '''
        pass

    def num_rows_and_columns(self):
        '''(Matrix) -> int
        This use the parent class to get the int from the
        num_rows_and_columns.
        '''
        pass
    
    def add_matrix(self, matrix_2):
        '''(Matrix, Matrix) -> NoneType
        This will add the matrix by inheirting from the parent class
        add_matrix method.
        '''
        pass
    
    def subtract_matrix(self, matrix_2):
        '''(Matrix, Matrix) -> NoneType
        This will subtract the matrix by inheirting from the parent class
        subtract_matrix method.
        '''
        pass
    
    def multiply_matrix(self, matrix_2):
        '''(Matrix, Matrix) -> NoneType
        This will multiply the matrix by inheirting from the parent class
        multiply_matrix method.
        '''
        pass
    
    def get_value(self, row1, column1):
        '''(Matrix, int, int) -> int or str
        This will inheirt from the parent class get_value which will be able
        to obtain the int or str in the suggested row and column.
        '''
        pass
    
    def set_value(self, obj, row1, column1):
        '''(Matrix, int or str, int, int) -> NoneType
        This will inheirt from the parent class set_value which will be able
        to put the int or str in the suggested row and column.
        '''
        pass
    
    def set_diagonal(self, obj):
        '''(Matrix, int or str) -> NoneType
        This will get the dimensions of the square identity. Then it
        will get the range between the dimension and use parent class
        with set_value with (1,1), plus 1, till the dimension rep by n (n,n).
        '''
        pass
    
    def get_diagonal(self):
        '''(Matrix) -> NoneType
        This will inheirt from parent to obtain the diagonal of the square
        '''
        pass      
    
    def transpose_matrix(self):
        '''(Matrix) -> NoneType
        This will inheirt from the parent class transpose_matrix which will
        be able to convert the rows into columns.
        '''
        pass
    
    def swap_column(self, column1, column2):
        '''(Matrix, int, int) -> NoneType
        This will inheirt from the parent class swap_column which will be able
        to switch the columns in the list with the other.
        '''
        pass
    
    def swap_row(self, row1, row2):
        '''(Matrix, int, int) -> NoneType
        This will inheirt from the parent class swap_row which will be able
        to switch the rows in the list with the other.
        '''
        pass
    
    def get_row(self, row1):
        '''(Matrix, int) -> list
        This will inheirt from the parent class so it can obtain the row
        asked
        '''
        pass
    
    def set_row(self, obj_row, row1):
        '''(Matrix, list, int) -> NoneType
        This will inheirt from the parent class so it can change a row into
        a different one
        '''
        pass
    
    def get_column(self, column1):
        '''(Matrix, int) -> list
        This will inheirt from the parent class so it can get a column from
        the matrix.
        '''
        pass
    
    def set_column(self, obj_column, column1):
        '''(Matrix, list, int) -> NoneType
        This will inheirt from the parent class so it can change a column into
        the column asked
        '''
        pass    

class Symmetric(SquareMatrix):
    
    def __init__(self, matrix_list):
        '''(Matrix) -> NoneType
        This will make a matrix which is represented as a list that is
        symmetrical, first adds valid matrix by the desired dimensions.
        REQ: must be symmetrical
        '''
        pass

    def num_rows_and_columns(self):
        '''(Matrix) -> int
        This will inheirt from the parent class and count the number
        of columns and rows since if symmetric would be square so same
        dimensions.
        '''
        pass
    
    def add_matrix(self, matrix_2):
        '''(Matrix, Matrix) -> NoneType
        This will add the matrix by inheirting from the parent class
        add_matrix method.
        '''
        pass
        
    def subtract_matrix(self, matrix_2):
        '''(Matrix, Matrix) -> NoneType
        This will subtract the matrix by inheirting from the parent class
        subtract_matrix method.
        '''
        pass
        
    def multiply_matrix(self, matrix_2):
        '''(Matrix, Matrix) -> NoneType
        This will multiply the matrix by inheirting from the parent class
        multiply_matrix method.
        '''
        pass
        
    def get_value(self, row1, column1):
        '''(Matrix, int, int) -> int or str
        This will inheirt from the parent class get_value which will be able
        to obtain the int or str in the suggested row and column.
        '''
        pass
    
    def set_value(self, obj, row1, column1):
        '''(Matrix, int or str, int, int) -> NoneType
        This will set the value using the parent class set_value, then has the
        dimensions subtract the row and columns for the opposite position
        then use those dimensions to replace that side, so its still
        symmetrical.
        '''
        pass
    
    def get_row(self, row1):
        '''(Matrix, int) -> list
        This will inheirt from the parent class so it can obtain the row
        asked
        '''
        pass
    
    def set_row(self, obj_row, row1):
        '''(Matrix, list, int) -> NoneType
        This will inheirt from the parent class so it can change a row into
        a different one
        '''
        pass
    
    def get_column(self, column1):
        '''(Matrix, int) -> list
        This will inheirt from the parent class so it can get a column from
        the matrix.
        '''
        pass
    
    def set_column(self, obj_column, column1):
        '''(Matrix, list, int) -> NoneType
        This will inheirt from the parent class so it can change a column into
        the column asked
        '''
        pass

    def get_diagonal(self):
        '''(Matrix) -> NoneType
        This will inheirt from parent to obtain the diagonal of the square
        '''
        pass

    def set_diagonal(self, obj_list):
        '''(Matrix, list) -> NoneType
        This will inheirt from parent to obtain the diagonal of the square and
        replace with new diagonal of same dimenesions
        '''
        pass     