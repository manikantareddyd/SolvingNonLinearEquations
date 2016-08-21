class BairStow:
    def __init__(self):
        self.Threshold = 0.05
        self.maxIter = 20
        self.getData()
        roots = self.compute(self.polynomial)
        print(roots)
    def getData(self):
        print("Enter polynomial as coefficients only")
        self.polynomial =  list(map(complex, input().split(',')))
        print("Enter r")
        self.r = list(map(complex, input().split(',')))[0]
        print("Enter s")
        self.s = list(map(complex, input().split(',')))[0]
    
    def compute(self,polynomial):
        i=0
        r = self.r
        s = self.s
        b = [0 for x in polynomial]
        c = [0 for x in polynomial]
        polynomial.reverse()
        a = polynomial
        # print(len(polynomial))
        if(len(polynomial)==2):
            roots = [-a[0]/a[1]]
            return roots
        elif(len(polynomial)==3):
            x1 = complex(-0.5*a[1] + 0.5*cmath.sqrt((a[1]*a[1])-(4*a[0])))
            x2 = complex(-0.5*a[1] - 0.5*cmath.sqrt((a[1]*a[1])-(4*a[0])))
            roots = [x1,x2]
            return roots
        elif(len(polynomial)==1):
            return []
        else:
            pass
        
        while 1:
            b[-1]=a[-1]
            b[-2]=a[-2]+r*b[-1]
            t=len(a)-3
            while 1:
                b[t]=a[t]+ r*b[t+1]+s*b[t+2]
                t = t-1
                if(t<0): break
            # print("a",a)
            # print("b",b)
            # print("b",b)
            c[-1]=b[-1]
            c[-2]=b[-1]+r*c[-1]
            t = len(a) - 3
            while 1:
                # print("B",c[t])
                c[t]=b[t]+r*c[t+1]+s*c[t+2]
                # print("A",c[t])
                t = t - 1
                if(t<0): break

            # print(c)
            try:
                dels = complex((-(b[1]*c[1]-b[0]*c[2]))/(c[2]*c[2]*1.0-1.0*c[1]*c[3]))
            except:
                dels = complex(0)
            try:
                delr = complex((-(b[0]*c[3]-b[1]*c[2]))/(c[2]*c[2]*1.0-c[1]*1.0*c[3]))
            except:
                delr = complex(0)

            r = r - delr 
            s = s - dels
            # print(r,s,delr,dels) 
            if(abs(100*delr)<abs(r*self.Threshold) and abs(100*dels)<abs(s*self.Threshold)) or i>self.maxIter:
                x1 = complex(r*0.5 + cmath.sqrt((r*r)+(4*s))*0.5)
                x2 = complex(r*0.5 - cmath.sqrt((r*r)+(4*s))*0.5)
                # print("b",b)
                new_poly = b[2:]
                new_poly.reverse()
                # print("New Poly",new_poly)
                roots = [x1,x2] + self.compute(new_poly)
                self.r = r
                self.s = s
                break
            
            i = i + 1
        return roots

import cmath
a = BairStow()