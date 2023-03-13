#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()

    for a in range(len(new_list)):
        if idx < 0:
            return (my_list)
        elif idx >= (len(new_list)):
            return (my_list)
        elif idx == a:
            new_list[idx] = element
            return (new_list)
