import mysql.connector



mydb = mysql.connector.connect(host="localhost", username ="root", password ="", database = "dbsegur")

cursor =  mydb.cursor()

cursor.execute('SELECT * FROM area')

#area = cursor.fetchone()
areas = cursor.fetchall()

print(areas)

mydb.close()