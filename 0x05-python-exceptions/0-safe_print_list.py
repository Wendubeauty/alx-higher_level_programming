#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ind = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ind += 1
        except index_error:
            break
    print()
    return(ind)
