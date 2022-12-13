#! /usr/bin/python3

import sys


def nb_arg():
    if len(sys.argv) != 2:
        return False
    else:
        return True


def is_integer(argv):
    count = 0
    for char in argv:
        if chr(47) < char < chr(58):
            count = count + 1
        else:
            count = count - 1
    if count == len(argv):
        return True
    else:
        return False

def is_flot(user_input):
    count = 0
    for char in user_input:
        if chr(47) < char < chr(58) or char == chr(46):
            count = count + 1
        else:
            count = count - 1
    if count == len(user_input):
        return True
    else:
        return False
