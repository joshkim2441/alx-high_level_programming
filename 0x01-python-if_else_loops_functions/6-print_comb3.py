#!/usr/bin/python3
for nmb1 in range(10):
    for nmb2 in range(10):
        if nmb2 > nmb1 and nmb1 != 8:
            print("{}{}".format(nmb1, nmb2), end=", ")
        elif nmb1 == 8 and nmb2 == 9:
            print("{}{}".format(nmb1, nmb2))
            break
