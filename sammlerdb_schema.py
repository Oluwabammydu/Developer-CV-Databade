import mysql.connector as mariadb

mariadb_connection = mariadb.connect(host='localhost', user='root', password='bammy')
cursor = mariadb_connection.cursor()

#insert information
cursor.execute("use sammler")
cursor.execute("CREATE TABLE developers_profile (id INT(11)  AUTO_INCREMENT, name VARCHAR(100) NOT NULL, skills VARCHAR(255) NOT NULL, github_link VARCHAR(512) NOT NULL, file VARBINARY (3000) NOT NULL, PRIMARY KEY(id))")


#mariadb_connection.commit()
