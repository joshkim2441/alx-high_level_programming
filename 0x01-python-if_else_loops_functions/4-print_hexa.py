#!/usr/bin/python3
"""Print 0 to 98 in decimal and hexadecimal format"""

for number in range(0, 98):
    print("{} = {}".format(number, hex(number)))
