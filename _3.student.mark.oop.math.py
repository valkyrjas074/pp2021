import math
import numpy
import curses

#Student mark management
Students=[]
StudentID=[]
Courses=[]
CoursesID=[]
Mark=[]

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
    name = input("Enter student name: ")
    ID = input("Enter student ID: ")
    DoB = input("Enter student date of birth: ")
    student = Student(name,ID,DoB)
    Students.append(student)
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
    coursename = input("Enter course name: ")
    courseID = input("Enter course ID: ")
    credit = input("Enter credit: ")
    course = Course(coursename,courseID,credit)
    Courses.append(course)
#Student mark#
class mark:
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
    def inputMarks():
        courseName = input("Input course's name to input marks: ")
        for c in courses:
        if c.getName() == courseName:
           for s in students:
                mark = math.floor(float(input("Input " + s.getName() + "'s mark: ")))
                studentMark = StudentMark(s, c, mark)
                studentMarks.append(studentMark)
                s.setAvg(calculateAvg(s.getId()))

# Display
def ShowlistCourses():
    print("Show course List:")
    for c in courses:
        c.describe()


def ShowlistStudents():
    print("Show student List:")
    for s in students:
        s.describe()


def ShowMarks():
    courseName = input("Enter name of course to show marks: ")
    print("Student Marks for " + courseName)
    for studentMark in studentMarks:
        if courseName == studentMark.getCourse().getName():
            studentMark.describe()

# Average Calculation
def calculationAvg(id):
    marks = []
    for studentMark in studentMarks:
        if (studentMark.getStudent().getId() == id):
            marks.append(studentMark.getMark())
    return numpy.average(marks)



def showAvarage():
    id = input("Input student id: ")
    for s in students:
        if id == s.getId():
            print("Name: " + s.getName() + " Avg: " + str(s.getAvg()))

def sortAvg():
    sortedList = sorted(students, key=lambda x: x.gpa, reverse=True)
    for s in sortedList:
        s.describe()

def calculationWeightedSum(id):
    sum = 0
    for c in courses:
        smark = []
        warray = []
        for studentMark in studentMarks:
            if (studentMark.getStudent().getId == id):
                smark.append(studentMark.getMark())
                warray.append(c.etc)
        weights = numpy.array(warray)
        amark = numpy.array(smark)
        sum = sum + numpy.sum(numpy.dot(amark, weights))
    return sum

def showWeightedSum():
    id = input("Input student id: ")
    print("Weighted sum: " + str(calculateWeightedSum(id)))


# Main
def menu():
    option = "-1";
    while (option != "0"):
        print("""
                   MENU
            1. Add students
            2. Add courses
            3. Add marks
            4. Show student list
            5. Show course list
            6. Show mark list
            7. Calculate average score
            8. Calculate weighted sum
            9. Sort student list
            0. Exit
            """)
        option = input("Your option: ")
        if (option == "1"):
            AddInforStudent()
        elif (option == "2"):
            AddInforCourse()
        elif (option == "3"):
            inputMark()
        elif (option == "4"):
            ShowlistStudents()
        elif (option == "5"):
            ShowlistCourses()
        elif (option == "6"):
            ShowMarks()
        elif (option == "7"):
            showAvarage()
        elif (option == "8"):
            showWeightedSum();
        elif (option == "9"):
            sortAvg();
menu()
