import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost', 
    user='root', 
    passwd='Hayley2000'   
)


# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute('CREATE DATABASE elderco')

print('All done!!')
