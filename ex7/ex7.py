def rsum(list1):
    '''(list of int) -> int
    '''
    # this will check if there only one item
    if len(list1) == 1:
        # thats the only sum
        result = list1[0]
    else:
        # recursilvy calls the list and adds them up
        result = list1[0] + rsum(list1[1:])
    return(result)


def rmax(list1):
    '''(list of int) -> int
    '''
    # if there nothing the automatically makes it equal to 0
    if (list1 == []):
        result = int(0)
    else:
        # checks to run if any inner list
        if isinstance(list1[0], list):
            max1 = rmax(list1[0])
        else:
            # first part of list
            max1 = list1[0]
        # rest of list recursively
        left_max = rmax(list1[1:])
        # compares if one greater than the other
        if (max1 > left_max):
            result = max1
        else:
            result = left_max
        # returns the highest value
    return(result)


def second_smallest(list1):
    '''(list of int) -> int
    '''
    # finds min number
    min_num = rmin(list1)
    # base case only two elements
    if len(list1) == 2:
        if list1[0] > list1[1]:
            return(list1[0])
        else:
            return(list1[1])
    else:
        # recursivly calls until second
        '''
        x = second_smallest(list1[1:])
        y = list1[1]
        if min_val < x:
            if list1[1] < x:
                second_smallest = x
            else:
                second_smallest = -2
            return(second_smallest)
            '''
        x = -2
        return(x)


def sum_max_min(list1):
    '''
    (list) -> int
    '''
    # gets the maximum number
    max_val = rmax(list1)
    # gets the minimum number
    min_val = rmin(list1)
    # adds them up and returns
    result = max_val + min_val
    return(result)


def rmin(list1):
    '''
    HELPPER FUNCTION TO FIND THE
    MINIMUM NUMBER IN LIST
    '''
    # if only one element
    if len(list1) == 1:
        return(list1[0])
    else:
        # recursivley callls itself
        m = rmin(list1[1:])
        # compares and set min val
        if m > list1[0]:
            min_val = list1[0]
        else:
            min_val = m
        return(min_val)