class sample:

    def __init__(self,name1,name2):
        self.name1=name1
        self.name2=name2

    def fun(self):
        print("i like "+self.name1+ " and "+self.name2)

s=sample("python","java")

s.fun()