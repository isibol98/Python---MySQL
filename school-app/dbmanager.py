#!/usr/bin/env python3
from connection import connection
from student import Student
from teacher import Teacher
from class1 import Class
from mysql.connector import Error
from datetime import datetime
import time

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def getStudentById(self,id):
        self.cursor.execute(f"Select * From Student Where id = {id}")
        try:
            obj = self.cursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6])
        except Error as err:
            print("Error:", err)
        
    def getClasses(self):
        self.cursor.execute("Select * From class ")
        try:
            obj = self.cursor.fetchall()
            return Class.createClass(obj)
        except Error as err:
            print("Error:", err)

    def getStudentByClassId(self,classId):
        self.cursor.execute(f"Select * From Student Where id = {classId}")
        try:
            obj = self.cursor.fetchall()
            return Student.createStudent(obj)
        except Error as err:
            print("Error:", err)

    def addorEditStudent (self,student: Student):
        if id == 0:
            sql = "INSERT INTO Student(StudentNumber, Name, Surname, Birthdate, Gender, ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
            value = (student.studentNumber, student.name,student.surname,student.birthdate,student.gender,student.classId)
        else:
            sql = "Update student Set StudentNumber=%s, Name=%s, Surname=%s, Birthdate=%s, Gender=%s, ClassId=%s where id=%s"
            value = (student.studentNumber, student.name,student.surname,student.birthdate,student.gender,student.classId,student.id)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} student edited!")
        except Error as err:
            print("Error: ", err)

    def addTeacher(self,teacher: Teacher):
        pass

    def editTeacher(self,teacher: Teacher):
        pass

    def __del__(self):
        self.connection.close()
        print("Db has closed!")

if __name__ == "__main__":
    db = DbManager()

   # student = db.getStudentById()
