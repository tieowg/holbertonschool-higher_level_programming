#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) or idx < 0:
        return my_list.copy()
    else:
        newlist = []
        for i in range(len(my_list)):
            if i == idx:
                continue
            else:
                newlist.append(my_list[i])
        my_list = newlist.copu()
        return my_list
