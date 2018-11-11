from flask import Flask, render_template, url_for, request, redirect, flash
import mysql.connector as mariadb
import os
import pymysql
from flask_mysqldb import MySQL

app = Flask(__name__)

port = int(os.environ.get("PORT", 3306))

app.config['MYSQL_HOST'] = 'pfw0ltdr46khxib3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'zqcqd8wm0u73wqym'
app.config['MYSQL_PASSWORD'] = 'ccysgm4bx7jhzgug'
app.config['MYSQL_DB'] = 'nady2nvsj52l50go'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)




@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		name = request.form['name']
		skills = request.form['skills']
		github_link = request.form['githublink']
		cv_upload = request.form['file']

		# Create cursor
		cursor = mysql.connection.cursor()
		cursor.execute("INSERT INTO developers_profile(name, skills, github_link, file) VALUES('{}', '{}', '{}', '{}')".format(name, skills, github_link, cv_upload))
		
		# Commit to database
		mysql.connection.commit()

		# Close connection
		cursor.close()

		#flash('Your Profile have been saved, thanks for using Sammler')
		return redirect(url_for('status')) 
		
	return render_template('home.html')



@app.route('/about', methods=['GET','POST'])
def about():
	return render_template("about.html")


@app.route('/search', methods=['GET','POST'])
def to_search():
	if (request.method) == 'GET':
		rows = []
		return render_template('search.html' ,rows=rows)


	if(request.method) == 'POST':

		search = request.form['search']

		# Create cursor
		cursor = mysql.connection.cursor()

		# Get developer by search 
		result = cursor.execute("SELECT * FROM developers_profile WHERE skills = %s", [search])

		rows = cursor.fetchall()

		return render_template("search.html", rows=rows)
				
		cursor.close()
		

		
		
@app.route("/status", methods=['GET', 'POST'])
def status():
	return render_template('status.html')
	
	

if __name__ == '__main__':
	app.secret_key='secret_key'
	app.run(debug=True, host='0.0.0.0', port=port)