#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(len(i)):
            if j != 0:
                print(" ", end="")
            print("{:d}".format(i[j]), end="")
        print()
