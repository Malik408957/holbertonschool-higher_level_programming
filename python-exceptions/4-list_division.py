#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element from two lists and returns a new list.
    """
    result_list = []
    for i in range(list_length):
        result = 0
        try:
            element1 = my_list_1[i]
            element2 = my_list_2[i]
            if not isinstance(element1, (int, float)) or not isinstance(element2, (int, float)):
                print("wrong type")
                result = 0
            else:
                result = element1 / element2
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result_list.append(result)
    return result_listo

