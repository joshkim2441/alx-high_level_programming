#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_dgt = abs(number) % 10
if number < 0:
    l_dgt = -l_dgt

if l_dgt > 5:
    print(f"Last digit of {number} is {l_dgt} and is greater than 5")
elif l_dgt < 6 and l_dgt != 0:
    print(f"Last digit of {number} is {l_dgt} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {l_dgt} and is 0")
