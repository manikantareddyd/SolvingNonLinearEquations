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
            print(round(self.x[i+3],4),self.er[i])
    def readData(self):
        while 1:
            try:
                print("Please Enter x0,x1,x2 as 1,2,3")
                self.x = list(map(float, input().split(',')))
            except:
                print("\nOops!",sys.exc_info()[0],"Occured. Try again!")
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

    def dividedDiff1(self,a,b):
        return (self.Data.f(a),self.Data.f(b))/(a-b)

    def dividedDiff2(self,a,b,c):
        return (self.dividedDiff1(a,b)-self.dividedDiff1(b,c))/(a-c)

    def compute(self):
        self.f = []
        self.abc = []
        self.er = []
        i = 0
        while 1:
            if(i>self.maxIter): break
            self.f.append(self.Data.f(self.x[i+0]))
            self.f.append(self.Data.f(self.x[i+1]))
            self.f.append(self.Data.f(self.x[i+2]))
            #a = f[x0,x1,x2]
            self.abc.append(self.dividedDiff2(self.x[i+2],self.x[i+1],self.x[i+0]))
            #b = a(x2-x1)+f[x2,x1]
            self.abc.append(((self.abc[i+0])(self.x[i+2] - self.x[i+1]))+self.dividedDiff1(self.x[i+2],self.x[i+1]))
            #c = f(x2)
            self.abc.append(self.f.[i+2])
            
            
            delta = ((self.abc[i+1]**2)-(4*self.abc[i+0]*self.abc[i+2]))**0.5
            if(self.abc[i+1]<0):
                x3 = self.x[i+2] - (2*self.abc[i+2]/(self.abc[i+1]-delta))
            else:
                x3 = self.x[i+2] - (2*self.abc[i+2]/(self.abc[i+1]+delta))
            
            self.x.append(x3)
            try:
                self.er.append(100*abs(self.x[i+3]-self.x[i+2])/abs(self.x[i+3]))
                if(100*abs(self.x[i+3]-self.x[i+2])<= self.estError*self.x[i+3]): 
                    break
            except:
                self.er.append(1000)
            i = i + 1
