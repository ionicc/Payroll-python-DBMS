import sqlite3
from tkinter import *


class Constants:
    hra = 0.1
    da = 5000

def starter():
    print("\n\nPayroll System")
    print("==============")
    print("Please select one of the following options:\n\n")
    print("1.Add")
    print("2.Delete")
    print("3.Compute")
    print("4.Show all")
    print("99.Exit\n")


def takeInput(n):
    if n == 1:
        empId = input("Enter the ID:")
        name = input("Enter the name:")
        age = input("Enter the age:")
        salary = input("Enter the salary:")
        dept = input("Enter the department:")

        return empId,name, age, salary, dept
    if n == 2:
        empId = input("Enter the ID:")
        return empId


def main():
    conn = sqlite3.connect("payroll.db")
    while(1):
        starter()
        n = int(input())
        if(n == 1):

            empId, name, age, salary, dept = takeInput(1)
            com = "INSERT INTO EMPLOYEE (ID, NAME, AGE, SALARY, DEPT) VALUES({}, '{}', {}, {},'{}')".format(empId, name, age, salary, dept)
            conn.execute(com)

        if(n == 2):
            empId = takeInput(2)
            com = "DELETE FROM EMPLOYEE WHERE ID = {}".format(empId)
            conn.execute(com)

        if(n == 3):
            empId = takeInput(2)
            com = "SELECT SALARY FROM EMPLOYEE WHERE ID = {}".format(empId)
            cursor = conn.execute(com)
            for row in cursor:
                sal = row[0]
            totalSal = sal + sal*Constants.hra + Constants.da
            print("Total salary of Employee ID = {} is {}".format(empId, totalSal))                

        if(n == 4):
            cursor = conn.execute("SELECT id, name, age, salary, dept from EMPLOYEE")
            print("ID | NAME | AGE | SALARY | DEPT")
            for row in cursor:
                s = "{} | {} | {} | {} | {}".format(row[0], row[1], row[2], row[3], row[4])
                print(s)
        if(n == 99):
            break
        conn.commit()



if __name__ == "__main__":
    main()