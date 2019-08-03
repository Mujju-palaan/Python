class Name:
    #constructor method - instantiation
    def__init__(self,first,middle,last):
        self.first = first
        self.middle = middle
        self.last = last
    #to-string method
    def__str__(self):
        return self.first + ' ' +self.middle +' ' + self.last 

aName = Name('Mary','Elizabeth','Smith')
print("aName is " + str(aName))