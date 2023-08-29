#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real_len = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                real_len += 1
    except (TypeError, ValueError):
        pass
    finally:
        print()
        return real_len
