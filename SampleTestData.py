import mysql.connector as mariadb

mariadb_connection = mariadb.connect(host='localhost', user='root', password='bammybammy', database='samm')
cursor = mariadb_connection.cursor()

#insert information
cursor.execute("CREATE TABLE clients (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), skills VARCHAR(255))")

sql = "INSERT INTO clients (name, skills) VALUES (%s, %s)"
val = [
  ('Marshall', 'Javascript'),
  ('Emmanuel', 'Mysql'),
  ('Zokky', 'Pyhton'),
  ('Emeka', 'Dynamic Programming'),
]

cursor.executemany(sql, val)

mariadb_connection.commit()
print("The last inserted id was: ", cursor.lastrowid)
