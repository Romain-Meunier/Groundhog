#! /usr/bin/python3

from math import *
import sys

def calcul_value_r(line, val, number, stack, temp, stack_sto, list_pourcentage):
    sto = 0
    val = int(val)
    index = 0
    stack.append(line)
    if number < val:
        print("r=nan%", "     ", end="")
    else:
        index = index + 1
        sto = float(stack[number]) - float(stack[temp])
        sto = float(sto) / float(stack[temp])
        sto = sto * 100
        test = int(round(sto, 0))
        list_pourcentage.append(test)
        test = str(test)
        test = "r=" + test + '%'
        print(test, "     ", end="")