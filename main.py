from Data import *
from Bisection import *
from FalsePosition import *
from ModifiedFalsePosition import *
from NewtonRaphson import *
from Secant import *
from Muller import *
# from BairStow import *
a=Equation()
# b = Bisection(a)
# b = NewtonRaphson(a)
# b = Secant(a)
# b = FalsePosition(a)
# b=ModifiedFalsePosition(a)
b = Muller(a)