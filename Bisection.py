class Bisection:
    def __init__(self,Data):
        self.Data = Data
        print("You have chosen Bisection method of finding roots")
        self.xu = []
        self.fxu = []
        self.xl = []
        self.fxl = []
        self.xr = []
        self.fxr = []
        self.er = []
        self.readData()
        self.root = self.compute(self.bounds[0],self.bounds[1],self.estError,self.maxIter)
        self.printTable()
        print(self.root)

    def printTable(self):
        i=0
        while i<len(self.er):
            print(round(self.xl[i],4),'\t',round(self.fxl[i],4),'\t',round(self.xu[i],4),'\t',round(self.fxu[i],4),'\t',round(self.xr[i],4),'\t',round(self.fxr[i],4),'\t',round(self.er[i],4),'\n')
            i=i+1

    def readData(self):
        while 1:
            try:
                print("Please enter lower and upper bounds seperated by a comma.\nIf x_l=0.1 and x_u=-9, then you should enter\n0.1,-9")
                self.bounds = list(map(float, input().split(',')))
                break
            except:
                print("\nOops!",sys.exc_info()[0],"occured. Try again!")
        while 1:
            try:
                print("Please enter the maximum Number of iterations:")
                self.maxIter = float(input())
                break
            except:
                print("\nOops!",sys.exc_info()[0],"occured. Try again!")
        while 1:
            try:
                print("Please enter the maximum Estimation error:")
                self.estError = float(input())
                break
            except:
                print("\nOops!",sys.exc_info()[0],"occured. Try again!")

    def compute(self,a,b,estError, maxIter):
        c = (a+b)/2.0
        i = 0
        self.xu.append(b)
        self.xl.append(a)
        self.xr.append(c)
        self.fxu.append(self.Data.f(b))
        self.fxl.append(self.Data.f(a))
        self.fxr.append(self.Data.f(c))
        self.er.append(0)
        while i < maxIter:
            oldc = c
            if self.Data.f(c) == 0:
                return c
            elif self.Data.f(a)*self.Data.f(c) < 0:
                b = c
            else:
                a=c
            c = (a+b)/2.0
            self.xu.append(b)
            self.xl.append(a)
            self.xr.append(c)
            self.fxu.append(self.Data.f(b))
            self.fxl.append(self.Data.f(a))
            self.fxr.append(self.Data.f(c))
            try:
                self.er.append(abs(100*(c-oldc)/c))
                if abs(100*(c-oldc)/c) < estError:
                    break
            except:
                self.er.append(1000)
            i = i + 1
        return c
