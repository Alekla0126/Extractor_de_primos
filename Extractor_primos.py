import math

class Extractor(object):

    def __init__(self,low,high):
        self.list = []
        self.primo = []
        self.low = low
        self.high = high

    def initizalize(self):
        index = self.low
        while(index<self.high+1):
            self.list.insert(index,index)
            index = index + 1
        return list
    
    def extract(self):
        self.primo.clear
        prime = False
        for i in range(self.low,self.high):
            if(i>0):
                if ((math.factorial(i-1))+1) % i == 0:
                    self.primo.append(self.list[i])         
        return self.primo

def main():
    low = int (input("Limite inferiror"))
    high = int (input("Limite superior"))
    extractor = Extractor(low,high)
    extractor.initizalize()
    primos = extractor.extract()
    print(primos)
main()


