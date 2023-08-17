#!/usr/bin/python3
def uniq_add(my_list=[]):
    _list = set(my_list)
    number = 0
    for i in _list:
        number += i
    return (number)
