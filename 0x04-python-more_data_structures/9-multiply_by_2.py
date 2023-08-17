#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    fresh_directory = a_dictionary.copy()
    _list = list(fresh_directory.keys())
    for i in _list:
        fresh_directory[i] *= 2
    return (fresh_directory)
