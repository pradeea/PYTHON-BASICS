class animal():
    def __init__(self):
        print("animal init")

    def eat(self):
        print("this is animal eat")

    def sleep(self):
        print("this is animal sleep")

class dog(animal):

    def __init__(self):
        animal.__init__(self)

    

d=dog()
d.eat()
d.sleep()
