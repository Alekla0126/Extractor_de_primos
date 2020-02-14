import math

class Extractor(object):

    def __init__(self):
        self.list = [0 for i in range(1001)]
        self.primo = []

    def initizalize(self):
        index = 0
        while(index<1001):
            self.list[index] = index
            index = index + 1
        return list
    
    def extract(self):
        self.primo.clear
        prime = False
        for i in range(0,1001):
            if(i>0):
                if ((math.factorial(i-1))+1) % i == 0:
                    self.primo.append(self.list[i])         
        return self.primo

def main():
    extractor = Extractor()
    extractor.initizalize()
    primos = extractor.extract()
    print(primos)
main()


