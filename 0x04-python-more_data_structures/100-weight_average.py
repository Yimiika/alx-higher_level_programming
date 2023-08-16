#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0  # Return 0 if the list is empty
    else:
        numerator = list(map(lambda x: x[0] * x[1], my_list))
        totaldenominator = sum(map(lambda x: x[1], my_list))
        totalnumerator = sum(numerator)
        result = totalnumerator / totaldenominator
        return result
