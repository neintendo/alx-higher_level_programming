#!/usr/bin/python3
def element_at(my_list, idx):
    for a in range(len(my_list)):
        if idx < 0:
            return (None)
        elif idx >= (len(my_list)):
            return (None)
        elif idx == a:
            return (my_list[a])
