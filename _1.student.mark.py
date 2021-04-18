Students=[]
StudentID=[]
Course=[]
CourseID=[]
Mark=[]
def input_student_number():
    i = int(input("Enter the numbers of student:"))
    return i

def addStudent():
    print("Add a new student to the course:")
    info = {
        'StudentName': '',
        'StudentID': '',
        'DoB': ''
    }
    print("Enter StudentName:")
    info['StudentName'] = input()
    return StudentName
    print("Enter StudentID:")
    return StudentID
    info['StudentID'] = id = input()
    print("Enter date of birth:")
    return DoB
    info['DoB'] = input()
    Students.append(info)
    StudentID.append(id)

def input_number_Course():
    j = int(input("Enter the numbers of course:"))
    return j

def addCourse():
    print("Add a course:")
    infoCourse = {
        'CourseName': '',
        'CourseID': ''
    }
    print("Enter CourseName:")
    infoCourse['CourseName'] = input()
    print("Enter CourseID:")
    infoCourse['CourseID'] = CourseID = input()
    Course.append(infoCourse)
    CourseID.append(CourseID)

def Mark():
    print("Enter student Mark:")
    infoMark = {
        'CourseID': '',
        'StudentID': '',
        'Mark': ''
    }
    print("Enter CourseID")
    infoMark['CourseID'] = k = input()
    if k in CourseID:
        print("Enter StudentID:")
        infoMark['StudentID'] = k1 = input()
        if k1 in StudentID:
            print("Enter Mark:")
            infoMark['Mark'] = float(input())
        else:
            return -1
    else:
        return -1
    Mark.append(infoMark)

def ShowCourse():
    print("Show lists of Course:")
    for l in range(0, len(Course)):
        print("[", Course[l]['CourseName'], "]", "[", Course[l]['CourseID'], "]", )

def ShowStudent():
    print("Show lists of students:")
    for m in range(0, len(Students)):
        print("[", Students[m]['StudentName'], "]", "[", Students[m]['StudentID'], "]", "[", Students[m]['DoB'], "]", )

def ShowMark():
    print("Show mark of the student in the course:")
    for n in range(len(Students)):
        print("[", Mark[n]['CourseID'], "]", "[", Mark[n]['StudentID'], "]", "[", Mark[n]['Mark'], "]", )

def StudentManagement():
    print("""Please choose an option:
    1.  Input Course:
    2.  Stop """)
    option = int(input("Choose:"))
    if option == 1:
        Nco = input_number_Course()
        print("1. Add course:")
        print("2. Stop")
        option1 = int(input("Choose:"))
        if option1 == 1:
            for i in range(Nco):
                addCourse()
                Num = input_number_student()
                for i in range(Num):
                    print("1. Input student:")
                    print("2. Stop:")
                    option2 = int(input("Choose:"))
                    if option2 == 1:
                        for i in range(Num):
                            addStudent()
                            ShowCourse()
                            ShowStudent()
                            print("1.Add Mark:")
                            print("2.Stop:")
                            option3 = int(input("Choose:"))
                            if option3 == 1:
                                Mark()
                                ShowCourse()
                                ShowStudent()
                                ShowMark()
                                break
                            else:
                                exit()
                    else:
                        exit()
        else:
            exit()
    else:
        exit()
StudentManagement()
ShowMark()