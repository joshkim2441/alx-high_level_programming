#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        if isinstance(my_list[i], int):
            try:
                print(my_list[i]), end="")
            except IndexError:
                break
        else:
            continue
        count += 1
    print()
    return count
