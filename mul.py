class Alpha:
    def fun1(self):
        print("iam an Alpha")
class Beta(Alpha):
    def fun2(self):
        print("iam an Beta")
class Gamma(Beta):
    pass
g=Gamma()
g.fun1()
g.fun2()
