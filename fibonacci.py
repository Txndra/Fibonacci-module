class Fibonacci:
    def __init__(self):
        self.num = self.getNum()
        self.fibList = []
        self.getSequence()
        self.displaySequence()
        self.resetSequence()

    def getNum(self):
        try:
            num=int(input("Enter a number: "))
            while num<=0:
                num =int(input("Error. Try again: "))
        except TypeError:
            num=int(input("Wrong data type loser. Try again: "))
        return num

    def getSequence(self):
        first=0
        second=1
        count=0
        while count < int(self.num):
            self.fibList.append(second)
            new = first + second
            first = second
            second = new
            count += 1

    def displaySequence(self):
        print("Your fibonacci sequence up to term ", self.num, ":")
        print(self.fibList[0], end = '')
        if (len(self.fibList) > 1):
            for i in range(1, len(self.fibList)):
                print(', ',self.fibList[i], end = '')

    def resetSequence(self):
        self.fibList = []
        
x = Fibonacci()
