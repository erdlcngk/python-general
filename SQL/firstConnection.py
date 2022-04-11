import mysql.connector
import numpy as np

def getStuden(name,surname):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "tazimcan452",
        database = "schooldb"
    )
    connection = mydb.cursor(buffered=True)
    name,surname = f"%{name}%", f"%{surname}%"

    request = "SELECT * FROM student WHERE name LIKE %s and surname LIKE %s"
    params = (name,surname)
    connection.execute(request,params)
    result = connection.fetchall()
    print(result)
    connection.close()
getStuden("mir","ö")





