#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    _list = list(a_dictionary.keys())
    for _dic in _list:
        if value == a_dictionary.get(_dic):
            del a_dictionary[_dic]
    return (a_dictionary)
