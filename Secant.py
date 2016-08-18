class Secant:
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

    def printTable(self):
        i=0
        while i<len(self.er):
            print(round(self.xr[i+2],4),'\t',round(self.fxr[i],4),'\t',round(self.dfxr[i],4),'\t',round(self.er[i],4),'\n')
            i=i+1

    def readData(self):
        while 1:
            try:
                print("Please enter x0")
                self.xo =  list(map(float, input().split(',')))[0]
                # self.xo = 0.5
                break
            except:
                print("\nOops!",sys.exc_info()[0],"occured. Try again!")
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
                self.estError = list(map(float, input().split(',')))[0]
                if(self.estError < 0):
                    print("Wait! error has to be positive")
                    continue
                break
            except:
                print("\nOops!",sys.exc_info()[0],"occured. Try again!")
        while 1:
            try:
                print("Please enter the x_(-1) and x_(0)")
                self.xs = list(map(float, input().split(',')))
                if(len(self.xs) != 2):
                    print(self.xs)
                    continue
                # self.xs = [0.1,1.0]
                break
            except:
                print("\nOops!",sys.exc_info()[0],"occured. Try again!")

    def compute(self,xo,estError, maxIter):
        c = xo
        i = 0
        self.xr.append(self.xs[0])
        self.xr.append(self.xs[1])
        self.xr.append(c)
        self.fxr.append(self.Data.f(c))
        self.dfxr.append(self.sec())
        self.er.append(0)
        while i < maxIter:
            oldc = c
            df = self.sec()
            c = oldc - (self.Data.f(oldc)*df)
            self.xr.append(c)
            self.fxr.append(self.Data.f(c))
            self.dfxr.append(df)
            try:
                self.er.append(abs(100*(c-oldc)/c))
                if abs(100*(c-oldc)/c) < estError:
                    break
            except:
                self.er.append(1000)
            i = i + 1
        return c

    def sec(self):
        a = self.xr[-3]
        b = self.xr[-2]
        return (a - b)/(1.0*(self.Data.f(a)-self.Data.f(b)))
