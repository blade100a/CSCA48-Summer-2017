############
# Harri Pahirathan
# CSCA48
# Summer
# 2017-05-11
############


def greeting(name_1):
    '''
    (str)-> string
    This function will return a senetence with the following
    parameter in the sentence
    REQ: Must be a string
    >>>greeting("Bob")
    "Hello Bob how are you today?"
    >>>greeting("brian")
    "Hello brian how are you today?"
    '''
    # returns the statement with the parameter in it
    return("Hello " + name_1 + " how are you today?")


def mutate_list(list_1):
    '''
    (List) -> List
    This function will modifiy the list with the specific
    modifications as followed in exercise 0 pdf
    REQ: must contain one element atleast
    >>>list_1 = [1, 2, 3, "hello", True]
    >>>mutate_list(list_1)
    >>>print(list_1)
    ['Hello', 4, 6, "ell", False]
    '''
    # this will loop throguht all elements in list
    for x in range(len(list_1)):
        # checks if element type is int
        if (type(list_1[x]) == int):
            # multiplies the element by 2
            list_1.insert(x, (list_1[x]*2))
            list_1.pop(x+1)
        # checks if element type is boolean
        elif (type(list_1[x]) == bool):
            # it will change it to opposite boolean
            list_1.insert(x, not(list_1[x]))
            list_1.pop(x+1)
        # checks if element type is string
        elif (type(list_1[x]) == str):
            # takes the very first and last characters in string
            list_1.insert(x, (list_1[x])[1:-1])
            list_1.pop(x+1)
    # adds hello to the very first element of list
    list_1[0] = "Hello"


def merge_dicts(dic_1, dic_2):
    '''
    (dict, dict) -> dict
    This takes in two dictionaries and put two same keys together
    and the rest together to form one dictionary
    REQ: must have int
    >>>d1 = {'1': [2, 3, 7], '2': [3, 4]}
    >>>d2 = {'2': [0], '3': [4, 0]}
    >>>merge_dicts(d1, d2)
    {'1': [2, 3, 7], '2': [3, 4, 0], '3': [4, 0]}
    '''
    # this copies the first dictionary into the final product
    final_dic = dic_1.copy()
    # loops through second dict
    for x in dic_2:
        # check if key is in product
        if x in final_dic:
            # adds the elements of the key into the product same key
            final_dic[x] += dic_2[x]
        # if the key is not in the product
        else:
            final_dic[x] = dic_2[x]
    # returns the both dicts together
    return(final_dic)