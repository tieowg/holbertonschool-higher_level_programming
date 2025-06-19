#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    element = my_list[idx]
    else:
        print("Element at index {:d} is {}".format(idx, element))
