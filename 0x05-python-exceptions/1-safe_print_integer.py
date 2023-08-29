#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_len = 0
    try:
        for i in range(x):
            print("{:d}".format(i))
            real_len += 1
            return True
    except TypeError:
        return False
