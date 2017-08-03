def rsum(list1):
    # the list is empty
    if len(list1) == 0:
        total_sum = 0
    # the list has one but no inner list
    elif len(list1) == 1 and not(isinstance(list1[0], list)):
        total_sum = list1[0]
    # inner list
    elif isinstance(list1[0], list):
        rest_list = rsum(list1[1:])
        total_sum = rsum(list1[0]) + rest_list
    # recurislvy does it
    else:
        rest_list = rsum(list1[1:])
        total_sum = list1[0] + rest_list
    return(total_sum)


def rmax(list1):
    '''(list of int) -> int
    '''
    # if there is nothing max is 0
    if (list1 == []):
        result = int(0)
    else:
        # checks to run if any inner list
        if isinstance(list1[0], list):
            max_num = rmax(list1[0])
        else:
            # list beginning
            max_num = list1[0]
        # rest of list recursively
        left_max_num = rmax(list1[1:])
        # compares each other
        if (max_num > left_max_num):
            result = max_num
        else:
            result = left_max_num
        # returns max value
    return(result)


def second_smallest(list1):
    '''
    '''
    pass


def sum_max_min(list1):
    '''
    '''
    # gets the maximum number
    max_int = rmax(list1)
    # gets the minimum number
    min_int = rmin(list1)
    # adds them both up
    total = max_int + min_int
    return(total)


def rmin(list1):
    '''
    '''
    # if only one element and no inner list
    if len(list1) == 1 and not(isinstance(list1[0], list)):
        return(list1[0])
    # if theres nothing
    elif len(list1) == 0:
        return(int(99999999999))
    # if theres a inner list
    elif len(list1) == 2 and isinstance(list1[0], list):
        m = rmin(list1[1:])
        inner_list = rmin(list1[0])
        if inner_list < m:
            min_int = inner_list
        else:
            min_int = m
    else:
        # recursivley callls itself
        m = rmin(list1[1:])
        # compares and set min val
        if m > list1[0]:
            min_int = list1[0]
        else:
            min_int = m
        return(min_int)