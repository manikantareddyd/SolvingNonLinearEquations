import sys
import parser
from math import *
from sympy import *
import numpy as np

class Equation:
    def __init__(self):
        while 1:
            try:
                print("Please enter equation using standard system notation.\nNote:The Independent Variable should be x")
                self.equation = input()
                # self.equation = "(600*(x^4))-(500*(x^3))+(200*(x^2))-(20*x)-1"
                
                if(self.equation == "exit"):
                    break
                print(self.equation)
                break
            except:
                print("\nOops!",sys.exc_info()[0],"occured. Try again!")

    def f(self,voo):
        x = Symbol('x')
        y = sympify(self.equation)
        val = y.subs(x,voo*1.0)*1.0
        return val

    def df(self,voo):
        x = Symbol('x')
        y = sympify(self.equation)
        yprime = y.diff(x)
        f = lambdify(x, yprime, 'numpy')
        val = f(voo*1.0)*1.0
        return val
