#! /usr/bin/python3

from math import *
import sys

def calcul_value_s(user_input, period, comp, comp2, sto, stack_s):
    stack_s.append(user_input)
    toto = sum(stack_s)
    print(stack_s)