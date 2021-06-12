import mysql.connector

serverName = "localhost"
dbUserName = "root"
dbPassword = ""
dbName = "Medicine System"

try:
    conn = mysql.connector.connect(host=serverName, user=dbUserName, password=dbPassword, database=dbName)
    print('Successfuly connected!')
except:
    print('Connection failed!')



# from DbHandler import *
#
# c = conn.cursor()
#
# c.execute('Select * from department')
# row = c.fetchall()
# print(row)
