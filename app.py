from flask import Flask, render_template, url_for, request, redirect, flash
import mysql.connector as mariadb

app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		# $variable = $_POST['name_of_select'];
		name = request.form['name']
		skills = request.form['skills']
		github_link = request.form['githublink']
		cv_upload = request.form['file']
		conn = mariadb.connect(user='root',
							   password='bammy', 
							   database='sammler')
		cur = conn.cursor()
		query = "INSERT INTO developers_profile(name, skills, github_link, file) VALUES('{}', '{}', '{}', '{}')".format(name, skills, github_link, cv_upload)
		cur.execute(query)
		conn.commit()
		flash('Your Profile have been saved, thanks for using Sammler')
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

		conn = mariadb.connect(user='root',
								   password='bammy', 
								   database='sammler')
		cur = conn.cursor()
		query = "SELECT name,github_link FROM developers_profile WHERE skills LIKE %s"
		search = ('%'+search+'%', )
		cur.execute(query, search)
		rows = cur.fetchall()
		print(rows)
		cur.close()
		conn.close()
	#if rows not:
		flash('Skills not found in database')
		

		return render_template("search.html", rows=rows)

@app.route("/status", methods=['GET', 'POST'])
def status():
	return render_template('status.html')
	
	





if __name__ == '__main__':
	app.secret_key='secret_key'
	app.run(debug=True)