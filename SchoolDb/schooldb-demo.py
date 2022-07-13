from connection import mydb
from mysql.connector import Error
from datetime import datetime
import time

class Student:
    mydb = mydb
    mycursor = mydb.cursor()

    def __init__ (self, students):
        self.students = students

    @staticmethod
    def saveStudents(students):
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

    def updateStudent(self): #Add in choices?
        s.mycursor.execute("Update Student Set {newFilter}='{newInfo}' Where {filter}={search}") #... Set name='Ilkkan' Where name='Ali'
        try:
            s.mydb.commit()
            print(f"{s.mycursor.rowcount} student(s) updated!")
        except Error as err:
            print("Error: ", err)
            s.mydb.commit()
        finally:
            s.mydb.close()
            print("Database closed!")
    def deleteStudent (self): #Add in choices?
        s.mycursor.execute("Delete From Student Where id=1") #Change this later
        try:
            s.mydb.commit()
            print(f"{s.mycursor.rowcount} student(s) deleted!")
        except Error as err:
            print("Error: ", err)
            s.mydb.commit()
        finally:
            s.mydb.close()
            print("Database closed!")

students = []
s = Student(students)

choice = input("Welcome! What you want to do?\n1-Add New Student\n2-Check Students\n3-Search a Student\n4-Exit\n:")
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
            Student.saveStudents(students)
            break
elif choice == "2":
    s.getStudents()
elif choice == "3": #Create func for filter?
    filter = input("Search with ...\n1-Student Number\n2-Student Name\n3-Student Surname\n4-Student Gender\n")
    if filter == "1":
        filter = "studentnumber"
    elif filter == "2":
        filter = "name"
    elif filter == "3":
        filter = "surname"
    else:
        filter = "Gender"
    search = input(f"Enter Student {filter}:\n")
    s.searchStudents(filter, search)
else:
    print("Good bye...")
    time.sleep(4)


""""
    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNumber, Name, Surname, Birthday, Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentNumber, self.name,self.surname,self.birthday,self.gender)
        Student.mycursor.execute(sql,value)

        try:
            Student.mydb.commit()
            print(f"{Student.mycursor.rowcount} students added!")
        except Error as err:
            print("Error: ", err)
        finally:
            Student.mydb.close()
            print("Database closed!")
"""