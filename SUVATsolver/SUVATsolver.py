__author__ = 'Mike'

import math


def solveFma(var, val1, val2):
    if var == "F":
        return val1 * val2
    elif var == "m" | var == "a":
        return val1 / val2


def solvesutat(var, val1, val2, val3):
    if var == "s":
        return (val1 * val2) + ((val3 * math.pow(val2, 2))/2)
    elif var == "u":
        return (val1 - ((val3 * math.pow(val2, 2))/2))/val2
    elif var == "a":
        return (val1 - (val2 * val3))/(math.pow(val3, 2)/2)

print("Hello")
invar = input()
in1 = float(input())
in2 = float(input())
in3 = float(input())
print(solvesutat(invar, in1, in2, in3))