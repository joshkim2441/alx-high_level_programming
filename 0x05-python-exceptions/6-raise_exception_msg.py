#!/usr/bin/python3

def raise_exception_msg(message=""):
    try:
        raise_exception_msg("This is a name exception.")
    except NameError as e:
        print("Caught an exception: ", e)
