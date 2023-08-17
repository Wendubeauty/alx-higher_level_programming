#!/usr/bin/python3
def number_keys(a_dictionary):
    number = 0
    _list = list(a_dictionary.keys())
    for i in _list:
        number += 1
    return (number)
