import mysql.connector as mariadb

mariadb_connection = mariadb.connect(host='localhost', user='root', password='bammy')

cursor = mariadb_connection.cursor()

cursor.execute("CREATE DATABASE sammler")