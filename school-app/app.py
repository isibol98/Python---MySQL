#!/usr/bin/env python3
from dbmanager import DbManager

class App:
    def __init__(self):
        self.db = DbManager()


    def initApp(self):
        msg = "***\n1-Student List\n2-Add Student\n3-Edit Student\n4-Delete Student\n5-Add Teacher\n6-Lesson List\n7-Exit"
        while True:
            print(msg)
            choice = input("Choice: ")
            if choice == "1":
                app.displayStudent()
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass
            elif choice == "6":
                pass
            elif choice == "7":
                pass
            else:
                print("Try Again.")

    def displayStudent(self):
        classes = self.db.getClasses()
        for i in classes:
            print(f"{i.id}: {i.name}")
        classId = int(input("Class:"))
        students = self.db.getStudentByClassId(classId)
        print("Student List:")
        for index,std in enumerate(students):
            print(f"{index+1}-{std.name} {std.surname}")

if __name__ == "__main__":
    app = App()
    app.initApp()
 
