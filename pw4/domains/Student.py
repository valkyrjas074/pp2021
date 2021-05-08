#Students info#
class  Students:
    def __init__(self,name,ID,DoB):
        self.__name=name
        self.__ID=ID
        self.__DoB=DoB
    def describe(self):
        print(self.__name + " " + self.__ID + " " + self.__DoB)
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getAvg(self):
        return self.__avg
    def setAvg(self, avg):
        self.__avg = avg