class Bisection:
    def __init__(self,Data):
        self.Data = Data
        self.relApproxError = []
        print("You have chosen Bisection method of finding roots")

        self.readData()
        self.root = self.compute(self.bounds[0],self.bounds[1],self.estError,self.maxIter)

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
        while abs((b-a)/2.0) > estError and i < maxIter:
            oldc = c
            if self.Data.f(c) == 0:
                return c
            elif self.Data.f(a)*self.Data.f(c) < 0:
                b = c
            else:
                a=c
            c = (a+b)/2.0
            i = i + 1
            self.relApproxError.append(c)
            # print(i,c, abs((c - oldc)*100.0/c) , a,b)
        return c
