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

def remove_dictionary_items(dict):
    """
    remove_dictionary_items() takes a dictionary (dict) as input and removes
    any items where the values are not valid phone numbers. A valid phone number
    is defined as a string of 10 digits with no other characters.
    The function first check if the dictionary is empty and if yes,
    returns -1. If the dictionary is not empty, now the function checks for
    the items with invalid phone number format and removes them from
    the dict and returns the new updated dictionary. If there is no invalid value, returns the dict.
    Examples:
    - If dict is {'John': '0123456789', 'Doe': '987654321', 'Jane': '1234567890'},
      the function returns {'John': '0123456789', 'Jane': '1234567890'}.
    - If dict is {'Support': '1AF567^901', 'Service': '0123456789'},
      the function returns {'Service': '0123456789'}.
    Make sure to have different assert statements to test the function
    than the ones provided above. Note: Please refer to Zybooks 7.11 for more information on dictionaries.
    """
    if len(dict) == 0:
        return -1
    keys_to_remove = [key for key, value in dict.items() if
                      not (isinstance(value, str) and value.isdigit() and len(value) == 10)]
    for key in keys_to_remove:
        dict.pop(key)
    return dict


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

def sum_of_diagonal(matrix):
    """
    The function takes a 2D list (matrix) as input, where each sublist represents a row of the matrix.
    It returns the sum of the primary (top-left to bottom-right) diagonal if the matrix is square.
    If the matrix is not square or empty, the function returns -2 or -1, respectively.

    For example, if the input matrix is:
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

    The primary diagonals is 1+5+9 = 15, so the result output should be 15.
    """
    if not matrix or not matrix[0]:  # Check if the matrix is empty
        return -1

    n = len(matrix)  # Number of rows in the matrix

    # Check if the matrix is square
    for row in matrix:
        if len(row) != n:
            return -2  # Not a square matrix

    primary_diagonal_sum = 0

    for i in range(n):
        primary_diagonal_sum += matrix[i][i]  # Sum elements from top-left to bottom-right

    return primary_diagonal_sum

def slice_list(num_list, start, slice_length):
    """
    slice_list() takes a list (num_list), an nonnegative integer (starting position), and another nonnegative integer (slice length)
    The functions returns the sliced list by starting from `start` with length of `slice_length`, stride equals to 1.
    Assume `start` and `slice_length` are integers, and `num_list` as list.

    For example: If num_list = [1, 2, 3, 4, 5], start = 3, length = 2, return value is [4, 5]
                 If num_list = [1, 2, 3, 4, 5], start = 3, length = 0, return value is []

    If `num_list` is empty, return -1
    If `start` is negative or out of bound, return -1
    If slicing using `slice_length` is out of bound, return -1
    For example: If num_list = [1, 2, 3, 4, 5], start = -6, length = 2, return value is -1.
                 If num_list = [1, 2, 3, 4, 5], start = 2, length = -2, return value is -1.
                 If num_list = [1, 2, 3, 4, 5], start = 3, length = 3, return value is -1.

    Note: Please refer to Zybooks 7.6 for more information on slicing lists.
    """
    if len(num_list) == 0:
        return -1
    if start < 0 or slice_length < 0:
        return -1
    end = start + slice_length
    if end > len(num_list):
        return -1
    return num_list[start:end]

def calculate_average_scores(score_dict):
    """
    calculate_average_scores() takes a dictionary (score_dict) as input.
    The function calculates the average score of each students and output a dictionary in the format of 
    {student_name1: average_score1, student_name2: average_score2,...}
    If the score_dict is empty, function returns -1.
    If any of the keys is not of the string type, function eturn -2.
    For example: If the score_dict is {'Andrew': [10, 10, 10, 10, 10], 'Alan': [10, 20, 5, 10, 10]}, the function should
    calculate each student's average score and return a new dictionary {'Andrew': 10, 'Alan': 11}
    Note: Please refer to Zybooks 7.12.1 for more information on this function.
    """
    if score_dict == {}:
        return -1
    calculated_average = {}
    for key, value in score_dict.items():
        if type(key) != str:
            return -2
        average_score = sum(value) / len(value)
        calculated_average[key] = average_score
    return calculated_average

def sort_by_length(str_list): # Based on 7.9
    """
    sort_by_length() takes a list of strings (str_list).
    The function then checks if the list is empty; if yes, it returns -2.
    If the list is not empty, the function returns a copy of str_list that is sorted by the length of its contained strings.
    For example, If the list is ["Apple", "Pie", "Computer", "I"] the function should return the sorted list with
    the values ["I", "Pie", "Apple", "Computer"].
    If str_list contains a value that isn't a string, then return the statement 'List contains a type that is not a string!'
    Note: Please refer to Zybooks 7.9 for more information on sorting lists.
    """
    if len(str_list) == 0:
        return -2
    for val in str_list:
        if type(val) != str:
            return "List contains a type that is not a string!"
    return sorted(str_list, key=len)

def calculate_class_midterm_average(grades_dict):
    """
    Given a dictionary of student grades, this function calculates the class' 
    average score on the midterm.

    For example if the grades_dict is 
    {
        'John Ponting': {
            'Midterm': 80,
            'Final': 92
        },
        'Jacques Kallis': {
            'Midterm': 90,
            'Final': 75
        },
        'Ricky Bobby': {
            'Midterm': 40,
            'Final': 65
        }
    }
    the function should return (80 + 90 + 40) / 3 = 70

    If the grades_dict is empty, the function returns -1.
    If any of the keys is not of the string type, the function returns -2.

    Note: Please refer to Zybooks 7.13 for more information on dictionary nesting.

    Params:
    grades_dict (dict): dictionary of student grades.

    Returns:
    float: the class' average score on the midterm
    """
    if grades_dict == {}:
        return -1
    
    midterm_scores = []
    for student, grades in grades_dict.items():
        if type(student) != str:
            return -2
        midterm_scores.append(grades['Midterm'])
    avg_midterm_score = sum(midterm_scores) / len(midterm_scores)
    return avg_midterm_score

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

    assert sum_of_diagonal([[]]) == -1, "Test with an empty matrix failed"
    assert sum_of_diagonal([[1, 2], [3, 4], [5, 6]]) == -2, "Test with a non-square matrix (more rows) failed"
    assert sum_of_diagonal([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == -15, "Test with a matrix containing"
    assert remove_dictionary_items({'John': '0123456789', 'Doe': '987654321', 'Jane': '1234567890'}) == {
        'John': '0123456789', 'Jane': '1234567890'}
    assert remove_dictionary_items({'Support': '1AF567^901', 'Service': '0123456789'}) == {
        'Service': '0123456789'}
    assert remove_dictionary_items({'a': 1234567890, 'b': '1234567890'}) == {'b': '1234567890'}
    assert remove_dictionary_items({}) == -1
    assert slice_list([1, 2, 3, 4, 5], 3, 2) == [4,5]
    assert slice_list([1, 2, 3, 4, 5], 3, 0) == []
    assert slice_list([], -6, 2) == -1
    assert slice_list([1, 2, 3, 4, 5], -1, 2) == -1
    assert slice_list([1, 2, 3, 4, 5], 2, -1) == -1
    assert slice_list([1, 2, 3, 4, 5], 3, 3) == -1
    assert calculate_average_scores({}) == -1
    assert calculate_average_scores({"Alan": [95, 88, 92, 85, 85]}) == {"Alan": 89}
    assert calculate_average_scores({3: [95, 88, 92, 85, 85]}) == -2
    assert sort_by_length([]) == -2
    assert sort_by_length(["Apple", "Pie", "Computer", "I"]) == ["I", "Pie", "Apple", "Computer"]
    assert sort_by_length(["Invalid", 123]) == "List contains a type that is not a string!"
    assert sort_by_length(["0", "Abraham", "Logs", "Pineapple"]) == ["0", "Logs", "Abraham", "Pineapple"]
    assert sort_by_length(["A", ""]) == ["", "A"]
    assert calculate_class_midterm_average({}) == -1
    grades = {"John": {"Midterm": 80, "Final": 70}, "Lucie": {"Midterm": 90, "Final": 100}}
    assert calculate_class_midterm_average(grades) == 85
    assert calculate_class_midterm_average({"John": {"Midterm": 80, "Final": 70}}) == 80
    assert calculate_class_midterm_average({123: {"Midterm": 80, "Final": 70}}) == -2
