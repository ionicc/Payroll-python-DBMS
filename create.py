import sqlite3

conn = sqlite3.connect('payroll.db')

conn.execute('''CREATE TABLE EMPLOYEE
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         SALARY         INT,
         DEPT        VARCHAR(50));''')

conn.close()
