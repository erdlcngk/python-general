import mysql.connector




mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tazimcan452",
    database = "schooldb"
)
mydb.cursor().execute("CREATE TABLE Student (Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, StudentNumber INT, Name VARCHAR(100) NOT NULL , Surname VARCHAR(100) NOT NULL, Birthdate DATE, Gender VARCHAR(1))")
