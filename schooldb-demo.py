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

students = [
        ("62","Can","Yilmaz",datetime(2000, 5, 17),"M"),
        ("63","Ali","Aga",datetime(1990, 12, 3),"M"),
        ("64","Burak", "Sek",datetime(1999, 5, 12), "M"),
        ("65","Sevgi", "Yilmaz",datetime(1997, 7, 7),"F")
    ]

Student.saveStudents(students)