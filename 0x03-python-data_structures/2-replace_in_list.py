#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for a in range(len(my_list)):
        if idx < 0:
            return (my_list)
        elif idx >= (len(my_list)):
            return (my_list)
        elif idx == a:
            my_list[idx] = element
            return (my_list)
