from sympy.plotting import plot
from sympy import *
import matplotlib.pyplot as plt
class NewtonRaphson:
    def __init__(self,Data):
        self.Data = Data
        print("You have chosen Newton Raphson method of finding roots")
        self.xr = []
        self.fxr = []
        self.dfxr = []
        self.er = []
        self.readData()
        self.root = self.compute(self.xo,self.estError,self.maxIter)
        self.printTable()
        print(self.root)
        self.makePlot()

    def makePlot(self):
        x = Symbol('x')
        f = self.Data.equation
        p1 = plot(f)
        plt.plot(self.er)
        plt.show()

    def printTable(self):
        i=0
        while i<len(self.er):
            print(round(self.xr[i],4),'\t',round(self.fxr[i],4),'\t',round(self.dfxr[i],4),'\t',round(self.er[i],4),'\n')
            i=i+1

    def readData(self):
        while 1:
            try:
                print("Please enter x0")
                self.xo =  list(map(float, input().split(',')))[0]
                break
            except:
                print("\nOops!",sys.exc_info()[0],"occured. Try again!")
        while 1:
            try:
                print("Please enter the maximum Number of iterations:")
                self.maxIter = list(map(int, input().split(',')))[0]
                break
            except:
                print("\nOops!",sys.exc_info()[0],"occured. Try again!")
        while 1:
            try:
                print("Please enter the maximum Estimation error:")
                self.estError = list(map(float, input().split(',')))[0]
                break
            except:
                print("\nOops!",sys.exc_info()[0],"occured. Try again!")

    def compute(self,xo,estError, maxIter):
        c = xo
        i = 0
        self.xr.append(c)
        self.fxr.append(self.Data.f(c))
        self.dfxr.append(self.Data.df(c))
        self.er.append(0)
        while i < maxIter:
            oldc = c
            c = oldc - (self.Data.f(oldc)/self.Data.df(oldc))
            self.xr.append(c)
            self.fxr.append(self.Data.f(c))
            self.dfxr.append(self.Data.df(c))
            try:
                self.er.append(abs(100*(c-oldc)/c))
                if abs(100*(c-oldc)/c) < estError:
                    break
            except:
                self.er.append(1000)
            i = i + 1
        return c
