import sys
class Equation:
    def __init__(self):
        while 1:
            try:
                print("Please enter coefficients in descending order of exponents seperated by ','.\nIf your function is 3(x^2)-1(x^1)+5.1. Then your input should be\n3,-1,0,5.1")
                self.coefficients = list(map(float, input().split(',')))
                break
            except:
                print("\nOops!",sys.exc_info()[0],"occured. Try again!")

    def f(self,x):
        n = len(self.coefficients) - 1
        i=0
        val = 0
        while(i<=n):
            val = val + self.coefficients[n-i]*(x**i)
            i = i+1
        return val

    def df(self,x):
        n = len(self.coefficients) - 1
        i = 0
        val = 0
        while i<=n:
            val = val + self.coefficients[i]*(n-i)*(x**(n-i-1))
            i = i+1
        return val
