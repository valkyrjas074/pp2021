#Main
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