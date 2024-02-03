class add:
    def __init__(self,a,b):
        self.A=a
        self.B=b 
class addition(add):
    def sum1(self):
        print("the addition of :",self.A+self.B)

x=addition(5,6)
x.sum1()