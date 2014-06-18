__author__ = 'Mike'
import SUVATsolver
solver = SUVATsolver
print("Welcome to the SUVAT solver")
while True:
    eq = input("Enter equation to solve:\n\t1. F=ma\n\t2. s=ut + 0.5at^2\n\t3. v^2 = u^2 + 2as\n")
    if eq == "1":
        invar = input("Enter variable to solve for\n")
        inval1 = input("Enter first variable\n")
        inval2 = input("Enter second variable\n")
        print(solver.solve_fma(invar, float(inval1), float(inval2)))
    elif eq == "2":
        invar = input("Enter variable to solve for\n")
        inval1 = input("Enter first variable\n")
        inval2 = input("Enter second variable\n")
        inval3 = input("Enter third variable\n")
        print(solver.solve_sutat(invar, float(inval1), float(inval2), float(inval3)))
    elif eq == "3":
        invar = input("Enter variable to solve for\n")
        inval1 = input("Enter first variable\n")
        inval2 = input("Enter second variable\n")
        inval3 = input("Enter third variable\n")
        print(solver.solve_vu2as(invar, float(inval1), float(inval2), float(inval3)))