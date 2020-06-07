import mysql.connector

cnx = mysql.connector.connect(user = "root", database = "perbankan")
cursor = cnx.cursor()
query = ("SELECT * FROM nasabah")
cursor.execute(query)
for i in cursor:
    print(i)
cursor.close()
cnx.close()
