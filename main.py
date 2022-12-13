#! /usr/bin/python3

import sys
from moy_r import calcul_value_r
from moy_g import calcul_value_g
from error import is_flot, is_integer, nb_arg

value = 0

def header():
    print('SYNOPSIS')
    print('   ./groundhog period\n')
    print('DESCRIPTION')
    print('   period', '      ', 'the number of days defining a period')


def display(g, r, s):
    print("g=", g, "    ", "r=", r, "%", "    ", "s=nan")


def check_value(number, val, temp, sto, comp, riri):
    stack = list()
    stack_g = list()
    stack_r = list()
    sto = int(sto)
    temp = int(temp)
    temp = 0
    temp = int(temp) - int(sto)
    new_list = list()
    list_pourcentage = list()
    nb_input = 0
    while True:
        try:
            user_input = input()
            if user_input.strip() == "":
                sys.exit(84)
            if user_input.strip() == "STOP":
                if nb_input < int(number):
                    sys.exit(84)
                else:
                    sys.exit(0)
            if is_flot(user_input) is not True:
                sys.exit(84)
            else:
                coco = calcul_value_g(float(user_input), number, riri, stack_g, comp, new_list)
                if coco == 0:
                    riri = riri - 1
                    comp = comp - 1
            calcul_value_r(user_input, number, val, stack, temp, stack_r, list_pourcentage)
            print("s=nan")
            val = val + 1
            temp = temp + 1
            comp = comp + 1
            riri = riri + 1
        except EOFError:
            sys.exit(84)
        nb_input = nb_input + 1


def main():
    sto = 0
    comp = 0
    riri = -1
    if nb_arg() is not True:
        sys.exit(84)
    else:
        argv = sys.argv[1]
        if argv == '-h':
            header()
        elif is_integer(argv) is True:
            check_value(sys.argv[1], sto, sys.argv[1], sys.argv[1], comp, riri)
        else:
            sys.exit(84)


if __name__ == '__main__':
    main()