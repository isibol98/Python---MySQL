from connection import mydb
from mysql.connector import Error
from datetime import datetime

class Student:
    mydb = mydb
    mycursor = mydb.cursor()

    def __init__ (self, studentNumber, name, surname, birthday, gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.gender = gender

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
    
    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO Student(StudentNumber, Name, Surname, Birthday, Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)

        try:
            Student.mydb.commit()
            print(f"{Student.mycursor.rowcount} students added!")
        except Error as err:
            print("Error: ", err)
        finally:
            Student.mydb.close()
            print("Database closed!")

students = []

while True:
    studentNumber = input("Student Number: ")
    name = input("Student Name: ")
    surname = input("Student Surname: ")
    birthday = datetime.fromisoformat(input("Student Birthday(YY-MM-DD): "))
    gender = input("Student Gender(M/F): ")

    students.append((studentNumber,name,surname,birthday,gender))

    progress = input("Do you want to continue?(Y/N)").upper()
    if progress == "N":
        print("Saving...")
        Student.saveStudents(students)
        break

