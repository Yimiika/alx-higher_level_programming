#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    j = len(my_list) - 1
    for i in my_list:
        print("{:d}".format(my_list[j]))
        j -= 1
