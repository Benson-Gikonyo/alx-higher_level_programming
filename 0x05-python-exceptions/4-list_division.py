#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    divides element by element 2 lists.

    Args:
        my_list_1 (list): can contain elements of any type
        my_list_2 (_type_): can contain elements of any type
        list_length (_type_): can contain elements of any type
    """
    new_list = []

    for num in range(list_length):
        answer = 0
        try:
            answer = my_list_1[num] / my_list_2[num]
        except (TypeError, ValueError):
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            new_list.append(answer)
    return (new_list)
