#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element from two lists and returns a new list.
    Args:
        my_list_1 (list): First list of elements
        my_list_2 (list): Second list of elements
        list_length (int): Length of the result list
    Returns:
        list: New list with division results, 0 for failed divisions
    """
    result_list = []
    for i in range(list_length):
        result = 0
        try:
            # Try to get elements from both lists
            element1 = my_list_1[i]
            element2 = my_list_2[i]
            # Check if elements are numbers - TypeError üçün
            if not isinstance(element1, (int, float)) or not isinstance(element2, (int, float)):
                print("wrong type")
                raise TypeError  # Xətanı yuxarıya atırıq
            # Perform division
            result = element1 / element2
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            # Bu artıq isinstance yoxlamasında tutulur
            pass
        finally:
            result_list.append(result)
    return result_list
