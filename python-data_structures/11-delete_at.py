#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) or idx < 0:
        return my_list.copy()
    for i in range(len(my_list)):
        if i == idx:
            continue
        print(my_list[i], end= "")
