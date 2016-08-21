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
        for i in range(0,len(self.er)):
            print(self.x[i+3],self.er[i])
            
    def readData(self):
        while 1:
            try:
                print("Please Enter x0,x1,x2 as 1,2,3")
                # self.x = list(map(float, input().split(',')))
                self.x = [complex(0.0),complex(0.5),complex(1.0)]
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
            h0 = complex(x1 - x0)
            h1 = complex(x2-x1)
            del0 = complex((self.Data.f(x1)-self.Data.f(x0))/h0)
            del1 = complex((self.Data.f(x2)-self.Data.f(x1))/h1)
            
            #a = f[x0,x1,x2]
            a = complex((del1-del0)/(h1+h0))
            self.abc.append(a)
            #b = a(x2-x1)+f[x2,x1]
            # b = complex(self.dividedDiff1(x2,x1)+self.dividedDiff1(x2,x0)-self.dividedDiff1(x1,x0))
            b = complex((a*h1)+del1)
            self.abc.append(b)
            #c = f(x2)
            c = complex(self.Data.f(x2))
            self.abc.append(c)
            
            # print("abc ",a,b,c)
            delta = (b*b) - (4*a*c)
            delta = complex(cmath.sqrt(delta))
            
            denom1 = complex(b+delta)
            denom2 = complex(b-delta)
            delx1 = complex((-2*c)/denom1)
            delx2 = complex((-2*c)/denom2)

            if(abs(delx1)>abs(delx2)):
                x3 = complex(x2 + delx2)
            else:
                x3 = complex(x2 + delx1)

            print("x3",x3)
            
            self.x.append(x3)
            try:
                err = complex(100*(1-x2/x3))
                err = abs(err)
                print("Error ", err)
                self.er.append(err)
                if(err<0.05): break
            except:
                print("Error ",1000,sys.exc_info())
                self.er.append(1000)
            i = i + 1
