#Classes defined example

class Worker:
    def __init__(self, name, pay):      #initialise when created
        self.name = name                #self is the new object
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]    #split on string blanks
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)     #update pay in place
       