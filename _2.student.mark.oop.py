#Student mark management
Students=[]
StudentID=[]
Courses=[]
CoursesID=[]
Mark=[]

#Students info#
class  Students:
    def __init__(self,name,ID,DoB):
        self.name=name
        self.ID=ID
        self.DoB=DoB
        Students.append(self) 
        StudentID.append(self.ID)
    def describe(self):
        print(["name:"],self.name, ["ID:"],self.ID, ["DoB:"],self.DoB)
    def input_number_student():
         StudentNumber=int(input("Please enter the numbers of student:"))
         return StudentNumber
    def inputStudent():
         print("Add a new student:")
         print("Enter student name:")
         name=input()
         print("Enter StudentID:")
         id=input()
         print("Enter date of birth:")
         DoB=input()
         Student(name,ID,DoB)

#Courses info#
class Courses:
    def __init__(self,coursename,courseID):
        self.coursename=coursename
        self.courseID=courseID
        Courses.append(self)
        CoursesID.append(self.courseID)
    def describe(self):
        print(["coursename:"],self.coursename, ["courseid:"],self.courseID)
    def input_number_courses():
        coursenumber=int(input("Enter the numbers of course:"))
        return coursenumber
    def inputCourses():
         print("Add new course:")
         print("Enter course name:")
         coursename=input()
         print("Enter CoursesID:")
         courseID=input()
         Course(coursename,courseID)

#Student mark#
class mark:
    def __init__(self,courseID,ID,marks):
        self.courseID=courseID
        self.ID=ID
        self.marks=marks
        mark.append(self)
    def describe(self):
        print(["CoursesID:"],self.courseID, ["StudentID:"],self.ID, ["mark:"],self.marks)
    def inputMark():
         print("Enter CoursesID")
         courseid=input()
         if courseid in CoursesID:
             print("Enter StudentID:")
             id=input()
             if id in StudentID:
                 print("Enter marks:")
                 marks=float(input())
             else:
                 return 0
         mark(courseID,ID,marks)

#Show student marks#
    def ShowCourses():
         print("Show lists of courses:")
         for i in range(0,len(Courses)):
             print("[",Course.describe(Courses[i]),"]",)
             return i
    def ShowStudent():
         print("Show lists of Student:")
         for i in range(0,len(Students)):
             print("[",Student.describe(Students[i]),"]",)
             return i
    def ShowMarks():
          print("Show marks of a student in the courses:")
          for i in range(0,len(Students)):  
              print("[",mark.describe(Mark[i]),"]",)
              return i
    def StudentManagement():  
         print("""Select option:
         1.  Input Courses:
         2.  Stop """)
         option=int(input("Please choose an option:"))
         if option==1:
             Nco=Course.input_number_courses()
             print("1. Add a course:")
             print("2. Stop")
             option1=int(input("Please choose an option:"))
             if option1==1:
                 for i in range(Nco):
                     Course.inputCourses()
                     Num=Student.input_number_student()
                     for i in range(Num):
                         print("1. Input a student:")
                         print("2. Stop")
                         option2=int(input("Please choose an option:"))
                         if option2==1:
                             for i in range(Num):
                                 Student.inputStudent()
                                 Start.ShowCourses()
                                 Start.ShowStudent()
                                 print("1. Add marks:")
                                 print("2. Stop:")
                                 option3=int(input("Please choose an option:"))
                                 if option3==1:
                                     mark.inputMark()
                                     Start.ShowCourses()
                                     Start.ShowStudent()
                                     Start.ShowMarks()
                                     break
                                 else:
                                   exit()
                         else:
                            exit()
             else:
                exit()