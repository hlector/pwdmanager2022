import mysql.connector

try:

    mydb = mysql.connector.connect(host="localhost", user="root", password="")
    mycursor = mydb.cursor()

    try:
        mycursor.execute("CREATE DATABASE IF NOT EXISTS pwdmanager2022")
        print("Database is created")
    except IOError as Err:
        print(Err, "Ooops")

    mytable = mysql.connector.connect(host="localhost", user="root", password="", database="pwdmanager2022")
    mycursor = mytable.cursor()
    table = "data"
    showtables = "SHOW TABLES"
    mycursor.execute(showtables)
    results = mycursor.fetchall()
    results_list = [item[0] for item in results]

    if table in results_list:
        print("Table is already in db!")
    else:

        mycursor.execute("CREATE TABLE data (appname varchar(50), pass varchar(50))")
        print("Table is created")

except IOError as Err:
    print(Err, "Ooooooooooopssssss")
