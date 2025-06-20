#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 ==0:
            print(True)
        else:
            new_list.append(False)
        print("is" if True  else "is not")
