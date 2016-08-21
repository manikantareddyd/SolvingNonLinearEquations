import math
import cmath
import sys
from sympy import *
class Muller:
    def __init__(self,Data):
        self.Data = Data
        print("You have chosen the Muller method")
        self.readData()
        self.compute()
        self.printTable()
    def printTable(self):
        i = 0
        while 1:
            if(i>self.maxIter): break
            print(self.x[i+3],self.er[i])
            i = i+1
    def readData(self):
        while 1:
            try:
                print("Please Enter x0,x1,x2 as 1,2,3")
                # self.x = list(map(float, input().split(',')))
                self.x = [complex(0.0,0.0),complex(0.1,0.0),complex(0.3,0.0)]
                break
            except:
                print("\nOops!",sys.exc_info()[0],"Occured. Try again!")
        while 1:
            try:
                print("Please enter the maximum Number of iterations:")
                self.maxIter = list(map(int, input().split(',')))[0]
                # self.maxIter = 20
                break
            except:
                print("\nOops!",sys.exc_info()[0],"occured. Try again!")
        while 1:
            try:
                print("Please enter the maximum Estimation error:")
                # self.estError = list(map(float, input().split(',')))[0]
                self.estError = 0.05
                break
            except:
                print("\nOops!",sys.exc_info()[0],"occured. Try again!")

    def dividedDiff1(self,a,b):
        return complex((self.Data.f(a)-self.Data.f(b))/(a-b))

    def dividedDiff2(self,a,b,c):
        return complex((self.dividedDiff1(a,b)-self.dividedDiff1(b,c))/(a-c))

    def compute(self):
        self.f = []
        self.abc = []
        self.er = []
        i = 0
        while 1:
            if(i>self.maxIter): break
            x0 = complex(self.x[i+0])
            x1 = complex(self.x[i+1])
            x2 = complex(self.x[i+2])
            self.f.append(complex(self.Data.f(x0)))
            self.f.append(complex(self.Data.f(x1)))
            self.f.append(complex(self.Data.f(x2)))
            #a = f[x0,x1,x2]
            a = complex(self.dividedDiff2(x2,x1,x0))
            self.abc.append(a)
            #b = a(x2-x1)+f[x2,x1]
            b = complex(self.dividedDiff1(x2,x1)+self.dividedDiff1(x2,x0)-self.dividedDiff1(x1,x0))
            self.abc.append(b)
            #c = f(x2)
            c = complex(self.f[i+2])
            self.abc.append(c)
            
            print("abc ",a,b,c)
            delta = (b*b) - (4*a*c)
            delta = complex(cmath.sqrt(delta))
            
            denom1 = complex(b+delta)
            denom2 = complex(b-delta)

            if(denom1.real > denom2.real):
                print("+")
                x3 = x2-(2*c/denom1)
            else:
                print("-")
                x3 = x2-(2*c/denom2)
            print("x3",x3)
            # else:
                # x3 = x2 - (2*c/(b+delta))
            try: x3 = simplify(x3.expand(complex=True))
            except: x3 = complex(x3)
            
            self.x.append(x3)
            try:
                err = 100*(1-x2/x3)
                try: err = simplify(abs(err).expand(complex=True))
                except: err = abs(err)
                print("Error ", err)
                self.er.append(err)
                # if(err<0.05): break
            except:
                print("Error ",1000,sys.exc_info())
                self.er.append(1000)
            i = i + 1
