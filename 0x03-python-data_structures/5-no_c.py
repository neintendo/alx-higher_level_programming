#!/usr/bin/python3
def no_c(my_string):
    arr_no_c = ""
    for a in range(len(my_string)):
        if my_string[a] != "C" and my_string[a] != "c":
            arr_no_c += my_string[a]
    return (arr_no_c)
