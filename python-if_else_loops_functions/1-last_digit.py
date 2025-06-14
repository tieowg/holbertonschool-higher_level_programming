#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    number1 = number % 10
else:
    number1 = -(abs(number) % 10)
if number1 == 0:
    print("Last digit of", number, "is", number1, "and is 0")
if number1 > 5:
    print("Last digit of", number, "is", number1, "and is greater than 5")
if number1 <= 6:
    print("Last digit of", number, "is", number1, "and is less than 6 and not 0")
