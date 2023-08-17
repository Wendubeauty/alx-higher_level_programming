#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    number = 0
    den = 0
    for _tuple in my_list:
        number += _tuple[0] * _tuple[1]
        den += _tuple[1]
    return (number / den)
