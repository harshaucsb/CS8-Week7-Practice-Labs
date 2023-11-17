## Given the stubs for the following function 
## and the main program, complete the implementation.
## Finish the assert statements to properly
## assert the result shown below (be careful 
## with the types of the variables).

## Make sure that your asserts test
## different branches/cases.


def get_dictionary_value(options, option):
    """
    get_dictionary_value() takes an dict (options) and a string (option).
    The functions check if the dictionary is empty and if yes,
    returns -1. If the dictionary is not empty, the function
    checks if the option is in the dictionary and if yes,
    returns the value associated with the option. If the option is not
    in the dictionary, the function returns the options available separated by comma and space.
    For example: If the dictionary is {'a': 1, 'b': 2, 'c': 3} and the option is 'b',
    the function returns 2. If the option is 'd', the function returns
    'The available options are - a, b, c'. If the fuction is called with an empty dictionary,
    the function returns -1. Make sure to have different assert statements to test the function
    than the ones provided above. Note: Please refer to Zybooks 7.10 for more information on dictionaries.
    """
    if len(options) == 0:
        return -1
    elif option in options:
        return options[option]
    else:
        return_str = "The available options are - "
        for key in options:
            return_str += key + ', '
        return return_str[:-2]

def get_maximum_odd(values):
    """
    get_maximum_odds() takes a list (values) of  postive integers and returns
    the largest odd integer in that list.  The function checks if the
    list is empty and if yes, returns -1.  If the list is not empty, the function
    iterates through the list and determines the largest odd number in the list.  If there are no odd integers
    in the list then the function returns -99.  If the list is [7, 40, 33, 56, 98], then the function returns the integer 33.
    If the function is called with an empty list, the function returns -1.
    Make sure to have different assert statements to test the function than the
    ones provided above.  Note: Please refer to Zybooks 7.3 for more information on Iterating through a list.
    """
    if len(values) == 0:
        return -1
    max_odd = -99
    for val in values:
        if val % 2 == 1:
            if val > max_odd:
                max_odd = val
    return max_odd

def modify_list(num_list):
    """
    modify_list() takes a list (num_list).
    The function modifies the list of numbers by adding their position value to the corresponding value in the list.
    For example: If the list is [1, 2, 3, 4, 5] the function should return the modified list with the values [1, 3, 5, 7, 9]
    If num_list contains a value that isn't an integer, then return the statement 'List contains type that is not an integer at position {pos}'
    where pos is first instance of the other type
    If num_list is empty, return -1
    Note: Please refer to Zybooks 7.7 for more information on modifying lists.
    """
    if len(num_list) == 0:
        return -1
    for i in range(len(num_list)):
        if type(num_list[i]) is int:
            num_list[i] += i
        else:
            return f'List contains type that is not an integer at position {i}'
    return num_list

def shift_list(my_list, direction, step):
    """
    Shifts the elements of a given list to the left or right by a specified number of steps.

    Parameters:
    my_list (list): The list whose elements are to be shifted. Return -1 if the list is empty
    d (int): The direction of the shift (-1 for left, 1 for right). Return -2 if d is not -1 or 1
    s (int): The number of steps to shift the elements. Return -3 if d is not an integer.

    Returns:
    list: A new list with the elements shifted in the specified direction by the specified number of steps.

    Raises:
    ValueError: If the direction is not -1 or 1.

    Example:
    >>> shift_list([1, 2, 3, 4, 5], 1, 2)
    [4, 5, 1, 2, 3]
    """
    if not my_list:
        return -1
    if direction not in [-1, 1]:
        return -2
    if not isinstance(step, int):
        return -3 
    
    if step == 0:
        return my_list

    n = len(my_list)
    shifted_list = [None] * n
    step = step % n

    for i, element in enumerate(my_list):
        if direction == -1:  # Shift left
            shifted_list[i - step] = element
        elif direction == 1:  # Shift right
            shifted_list[(i + step) % n] = element
        
    return shifted_list


if __name__ == "__main__":
    ### Write 3 assert statements
    ### to test the function
    assert get_dictionary_value({}, 'a') == -1
    assert get_dictionary_value({'a': 1, 'b': 2, 'c': 3}, 'b') == 2
    assert get_dictionary_value({'a': 1, 'b': 2, 'c': 3}, 'd') == 'The available options are - a, b, c'
    assert get_maximum_odd([7, 40, 33, 56, 98]) == 33
    assert get_maximum_odd([2, 22, 10, 56, 90]) == -99
    assert get_maximum_odd([]) == -1

    assert modify_list([1, 2, 3, 4, 5]) == [1, 3, 5, 7, 9]
    assert modify_list([1]) == [1]
    assert modify_list(['hello', 10]) == 'List contains type that is not an integer at position 0'
    assert modify_list([]) == -1
    assert modify_list([0.1, 'Kelly', 'h']) == 'List contains type that is not an integer at position 0'
    assert modify_list([1, 2, 3.5, 4, 5]) == 'List contains type that is not an integer at position 2'

    assert shift_list([], 1, 5) == -1
    assert shift_list(["Jason", 'Kelly', 'Tom'], 0, 1) == -2
    assert shift_list([1, 2, 3.5, 4, 5], 1, 2.1) == -3
    assert shift_list(["Jason", 'Kelly', 'Tom'], -1, 2) == ['Tom', "Jason", 'Kelly']
    assert shift_list([1, 2, 3.5, 4, 5], 1, 2) == [4, 5, 1, 2, 3.5]
    assert shift_list(["banana", "apple", "pineapple", "pear", "peach"], 1, 7) == ["pear", "peach", "banana", "apple", "pineapple"]
