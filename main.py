from Data import *
from Bisection import *
from FalsePosition import *
from ModifiedFalsePosition import *
from NewtonRaphson import *
from Secant import *
from Muller import *
from BairStow import *
print("Hi. Enter\n1 for Bisection\n2 for NewtonRaphson\n3 for Secant\n4 for FalsePosition\n5 for ModifiedFalsePosition\n6 for Muller\n7 for Bair Stow's\n'")
choice = list(map(float, input().split(',')))[0]
if choice == 1: 
    a=Equation()
    b = Bisection(a)
elif choice == 2: 
    a=Equation()
    b = NewtonRaphson(a)
elif choice == 3: 
    a=Equation()
    b = Secant(a)
elif choice == 4: 
    a=Equation()
    b = FalsePosition(a)
elif choice == 5: 
    a=Equation()
    b = ModifiedFalsePosition(a)
elif choice == 6: 
    a=Equation()
    b = Muller(a)
elif choice == 7:
    a = BairStow()
else: print("oops")