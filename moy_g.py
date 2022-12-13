#! /usr/bin/python3

from math import *
import sys

def calcul_value_g(user_input, period, comp, stack, comp2, new_list):
    stack.append(user_input)
    period = int(period)
    coucou=int()
    if comp > -1:
        stockage = stack[comp2] - stack[comp]
        if stockage < 0:
            stockage = 0
        new_list.append(round(stockage, 1))
    if period > len(new_list):
        print("g=nan", "     ", end="")
    if len(new_list) == period:
        coucou = "%.2f" % round(sum(new_list) / period, 2)
        coucou = str(coucou)
        coucou = "g=" + coucou
        print(coucou, "     ", end="")
        new_list.pop(0)
        stack.pop(0)
        return 0