import mysql.connector
from prettytable import PrettyTable
import secrets

my_table = PrettyTable()

connection = mysql.connector.connect(host='localhost', database='pwdmanager2022', user='root', password='')
if connection.is_connected():
    db_info = connection.get_server_info()

    print("Connected to MySQL", db_info)


while True:
    var3 = input(" --- Please Enter 'a' do display all data\n --- Please enter the name of your app\n --- Please enter 'q' to exit\n --- Please enter 'd' to select a record for deleting\n --- Please enter 'dall' to delete all data\n --- Please enter 'new' to add a new creds\n")

    if var3 == "new":

        #print("You entered", var)
        #data = numpy.random.rand(5, 2)

        while True:
            var = input("Please enter the name of site or app: ")
            if var != "":
                t = PrettyTable(['Name of application'])
                t.add_row([var])
                print(t)
                break

            elif var == "":
                print("Empty app name")


        while True:
            var2 = input("Please enter the password: ")

            #print("Your entered password")
            if var2 !="" and var2 !="rand":
                t2 = PrettyTable(['Password of application'])
                t2.add_row([var2])
                print(t2)
                break

            elif var2 == "rand":
                t2 = PrettyTable(['Password of application'])
                t2.add_row(["SOME_RANDOM"])
                print(t2)
                break

            elif var2 == "":
                print("Empty password")

        if var2 !="rand":

            mysql_insert_query = "INSERT INTO data (appname, pass) VALUES ('" + var + "', '" + var2 + "')"
            cursor = connection.cursor()
            cursor.execute(mysql_insert_query)

            print(cursor.rowcount, "Record inserted")
            connection.commit()
        elif var2 == "rand":
            # RANDOM VALUE FUNCTIONAL

            mysql_insert_query = "INSERT INTO data (appname, pass) VALUES ('" + var + "', '"+secrets.token_hex(nbytes=16)+"')"
            cursor = connection.cursor()
            cursor.execute(mysql_insert_query)

            print(cursor.rowcount, "Record inserted")
            connection.commit()

    elif var3 == "a":

        mysql_select_query = "SELECT * FROM data"
        cursor = connection.cursor()
        cursor.execute(mysql_select_query)
        records = cursor.fetchall()
        print("Total numbers of rows: ", cursor.rowcount)
        print("Printing each row")

        for row in records:
            #print("Appname = ", row[0])
            #print("Pass = ", row[1])

            t3 = PrettyTable(['Application name', 'Application password'])
            t3.add_row([row[0], row[1]])
            print(t3)

            #t2 = PrettyTable(['Password of application'])
            #t2.add_row([var2])
            #print(t2)


    elif var3 == "d":
        deletevalue = input("Please enter the name to delete\n")

        mysql_delete_query = "DELETE FROM data WHERE appname='"+deletevalue+"'"
        cursor.execute(mysql_delete_query)
        connection.commit()
        print(deletevalue," is deleted in case if it's exists")

    elif var3 == "dall":
        secret = input("Please enter a secret password\n")
        if secret == "12345":

            mysql_delete_query = "DELETE FROM data"
            cursor.execute(mysql_delete_query)
            connection.commit()
            print("All data is deleted")
        else:
            print("Incorrect secret password!")


    elif var3:
        if var3 == "q":
            exit()
        else:
            mysql_select_query = "SELECT * FROM data WHERE appname='"+var3+"'"
            cursor = connection.cursor()
            cursor.execute(mysql_select_query)
            records = cursor.fetchall()
            print("Total numbers of rows: ", cursor.rowcount)
            print("Printing each row")

            for row in records:
                # print("Appname = ", row[0])
                # print("Pass = ", row[1])

                t3 = PrettyTable(['Application name', 'Application password'])
                t3.add_row([row[0], row[1]])
                print(t3)


connection.commit()
cursor.close()