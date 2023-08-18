#!/usr/bin/python3
def to_subtract(list_num):
    total_to_subtract = 0
    max_number = max(list_num)
    for n in list_num:
        if max_number > n:
            total_to_subtract += n
    return (max_number - total_to_subtract)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
    _list = list(roman_numerals.keys())
    number = 0
    last_numeral_value = 0
    list_num = [0]

    for i in roman_string:
        for n in _list:
            if n == i:
                if roman_numerals.get(i) <= last_numeral_value:
                    number += to_subtract(list_num)
                    list_num = [roman_numerals.get(i)]
                else:
                    list_num.append(roman_numerals.get(i))
                last_numeral_value = roman_numerals.get(i)

    number += to_subtract(list_num)

    return (number)
