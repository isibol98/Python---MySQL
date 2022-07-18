#!/usr/bin/env python3
from connection import mydb
from mysql.connector import Error
from datetime import datetime
import time

def filter_ (a) -> str: # a -> Search/Update/Delete
    filter = input(f"{a} ...\n1-Student Number\n2-Student Name\n3-Student Surname\n4-Student Gender\n")
    if filter == "1":
        filter = "studentnumber"
    elif filter == "2":
        filter = "name"
    elif filter == "3":
        filter = "surname"
    elif filter == "4":
        filter = "Gender"
    else:
        print("Try again.")
        filter_()
    return filter

class StudentRepo:
    mydb = mydb
    mycursor = mydb.cursor()

    def __init__ (self, students):
        self.students = students

    def saveStudents(self,students):
        sql = "INSERT INTO Student(StudentNumber, Name, Surname, Birthday, Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        s.mycursor.executemany(sql,values)

        try:
            s.mydb.commit()
            print(f"{s.mycursor.rowcount} students added!")
        except Error as err:
            print("Error: ", err)
            s.mydb.commit()
        finally:
            s.mydb.close()
            print("Database closed!")

    def getStudents(self):
        s.mycursor.execute("Select * From Student Order By name") #Select name,surname From Student --student[0],student[1], Order by id ASC/DESC
        result = s.mycursor.fetchall() #fetchone()
        
        for student in result:
            print(f"Name: {student[2]}, Surname: {student[3]}")
    
    def searchStudents(self,filter,search):
        s.mycursor.execute(f"Select * From Student Where {filter}='{search}'")
        result = s.mycursor.fetchall()
        for student in result:
            print(student)

    def updateStudent(self,newFilter,newSearch,filter,search): 
        s.mycursor.execute(f"Update Student Set {newFilter}='{newSearch}' Where {filter}={search}") #... Set name='Ilkkan' Where name='Ali'
        try:
            s.mydb.commit()
            print(f"{s.mycursor.rowcount} student(s) updated!")
        except Error as err:
            print("Error: ", err)
            s.mydb.commit()
        finally:
            s.mydb.close()
            print("Database closed!")
    def deleteStudent (self,filter,search): 
        s.mycursor.execute(f"Delete From Student Where {filter}={search}")
        try:
            s.mydb.commit()
            print(f"{s.mycursor.rowcount} student(s) deleted!")
        except Error as err:
            print("Error: ", err)
            s.mydb.commit()
        finally:
            s.mydb.close()
            print("Database closed!")

if __name__ == "__main__":
    students = []
    s = StudentRepo(students)

    choice = input("Welcome! What you want to do?\n1-Add New Student\n2-Check Students\n3-Search a Student\n4-Update a Student's Data\n5-Delete a Student\n6-Exit\n:")
    if choice == "1":
        while True:
            studentNumber = input("Student Number: ")
            name = input("Student Name: ")
            surname = input("Student Surname: ")
            try:
                birthday = datetime.fromisoformat(input("Student Birthday(YY-MM-DD): "))
            except ValueError as err:
                print("Wrong input. Try again!")
                birthday = datetime.fromisoformat(input("Student Birthday(YY-MM-DD): "))
            gender = input("Student Gender(M/F): ")

            students.append((studentNumber,name,surname,birthday,gender))

            progress = input("Do you want to continue?(Y/N)").upper()
            if progress == "N":
                print("Saving...")
                time.sleep(3)
                s.saveStudents(students)
                break
    elif choice == "2":
        s.getStudents()
    elif choice == "3":
        filter = filter_("Search")
        search = input(f"Enter Student {filter}:\n")
        s.searchStudents(filter, search)
    elif choice == "4":
        newFilter = filter_("Update")
        filter = filter_("Find")
        newSearch = input(f"Enter the New {newFilter} Value: ")
        search = input(f"Enter Student {filter}:\n")
        s.updateStudent(newFilter,newSearch,filter,search)
    elif choice == "5":
        filter = filter_("Delete")
        search = input(f"Enter Student {filter}:\n")
        s.deleteStudent(filter,search)
    elif choice == "6":
        print("Shutting down...")
        time.sleep(2)
        quit()
    else:
        print("Try again.")

    

