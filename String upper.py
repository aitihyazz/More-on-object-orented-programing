class IOstring():
    def __init__(self):
        self.str1=''
    def getst(self):
        self.str1=input('Enter a string:')
    def printst(self):
        print("the result is:",self.str1.upper())
str1=IOstring()
str1.getst()
str1.printst()