#Input
import math
import numpy
import curses

def StudentInfo():
    name = input("Enter student name: ")
    ID = input("Enter student ID: ")
    DoB = input("Enter student date of birth: ")
    student = Student(name, ID, DoB)
    Students.append(student)


def CourseInfo():
    coursename = input("Enter course name: ")
    courseID = input("Enter course ID: ")
    credit = input("Enter credit: ")
    course = Course(coursename, courseID, credit)
    Courses.append(course)


def inputMarks():
    courseName = input("Input course's name to input marks: ")
    for c in courses:
        if c.getName() == courseName:
            for s in students:
                mark = math.floor(float(input("Input " + s.getName() + "'s mark: ")))
                studentMark = StudentMark(s, c, mark)
                studentMarks.append(studentMark)
                s.setAvg(calculateAvg(s.getId()))