#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for x, v in a_dictionary.items():
        new_dict[x] = v * 2
    return new_dict
