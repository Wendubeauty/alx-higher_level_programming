#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    _list = list(a_dictionary.keys())
    _list.sort()
    for i in _list:
        print("{}: {}".format(i, a_dictionary.get(i)))
