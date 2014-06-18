__author__ = 'Mike'

import math


def solve_fma(var, val1, val2):
    if var == "F":
        return val1 * val2
    elif (var == "m") | (var == "a"):
        return val1 / val2


def solve_sutat(var, val1, val2, val3):
    if var == "s":
        return (val1 * val2) + ((val3 * math.pow(val2, 2))/2)
    elif var == "u":
        return (val1 - ((val3 * math.pow(val2, 2))/2))/val2
    elif var == "a":
        return (val1 - (val2 * val3))/(math.pow(val3, 2)/2)
    elif var == "t":
        return {(-val2 + math.sqrt(math.pow(val2, 2) + 4 * val3 * -val1))/2 * val3, (-val2 - math.sqrt(math.pow(val2, 2) + 4 * val3 * -val1))/2 * val3}


def solve_vu2as(var, val1, val2, val3):
    if var == "v":
        return math.sqrt(math.pow(val1, 2) + (2 * val2 * val3))
    elif var == "u":
        return math.sqrt(math.pow(val1, 2) - (2 * val2 * val3))
    elif (var == "a") | (var == "s"):
        return (math.pow(val1, 2) - math.pow(val2, 2))/(2 * val3)


print("Welcome ot the SUVAT solver 9000")
while True:
    eq = input("Enter equation to solve:\n\t1. F=ma\n\t2. s=ut + 0.5at^2\n\t3. v^2 = u^2 + 2as\n")
    if eq == "1":
        invar = input("Enter variable to solve for\n")
        inval1 = input("Enter first variable\n")
        inval2 = input("Enter second variable\n")
        print(solve_fma(invar, float(inval1), float(inval2)))
    elif eq == "2":
        invar = input("Enter variable to solve for\n")
        inval1 = input("Enter first variable\n")
        inval2 = input("Enter second variable\n")
        inval3 = input("Enter third variable\n")
        print(solve_sutat(invar, float(inval1), float(inval2), float(inval3)))
    elif eq == "3":
        invar = input("Enter variable to solve for\n")
        inval1 = input("Enter first variable\n")
        inval2 = input("Enter second variable\n")
        inval3 = input("Enter third variable\n")
        print(solve_vu2as(invar, float(inval1), float(inval2), float(inval3)))