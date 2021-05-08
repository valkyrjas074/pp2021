#Output
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