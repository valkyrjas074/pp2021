#Courses info#
class Courses:
    def __init__(self,coursename,courseID, credit):
        self.__coursename=coursename
        self.__courseID=courseID
        self.__credit=credit
    def describe(self):
        print("Course name: " + self.__coursename + " CourseID: " + self.__courseID + " credit: " + self.__credit)
    def getName(self):
        return self.__name