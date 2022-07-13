from connection import mydb
from mysql.connector import Error

def insertStudents(list):
    cursor = mydb.cursor()

    sql = "INSERT INTO Student(StudentNumber, Name, Surname, Birthday, Gender) VALUES (%s,%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql,values)

    try:
        mydb.commit()
        print(f"{cursor.rowcount} student(s) added!")
        print(f"Last added student id: {cursor.lastrowid}")
    except Error as err:
        print("Error:", err)
    finally:
        mydb.close()
        print("Database closed.")

list = []

while True:
    studentNumber = input("Student Number: ")
    name = input("Student Name: ")
    surname = input("Student Surname: ")
    birthday = input("Student Birthday: ")
    gender = input("Student Gender(M/F): ")

    list.append((studentNumber,name,surname,birthday,gender))

    progress = input("Do you want to continue?(Y/N)").upper()
    if progress == "N":
        print("Saving...")
        insertStudents(list)
        break