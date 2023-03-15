#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for a in range(len(my_list)):
        new_list.append(my_list[a])
        if new_list[a] == search:
            new_list[a] = replace
    return (new_list)
