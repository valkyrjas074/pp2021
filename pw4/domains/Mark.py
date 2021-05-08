#Student mark#
class Mark:
    def __init__(self,student, course, marks):
        self.__student=student
        self.__course=course
        self.marks=marks
        mark.append(self)
    def getStudent(self):
        return self.__student
    def getCourse(self):
        return self.__course
    def getMarks(self):
        return self.__marks
    def describe(self):
        print(self.__student.getId() + " " + self.__student.getName() + " "
              + self.__course.getName() + " " + str(self.__marks))