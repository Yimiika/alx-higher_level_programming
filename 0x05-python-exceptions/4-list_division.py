#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
    for i in range(list_length):
       try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except (TypeError, ValueError, ZeroDivisionError):
            new_list.append(0)
            if not isinstance(my_list_1[i], (int, float)):
                print("wrong type")
            elif my_list_2[i] == 0:
                print("division by 0")
            else:
                print("out of range")
    finally:
        return new_list
