class Bisection:
    def __init__(self,Data):
        print("You have chosen Bisection method of finding roots")
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
