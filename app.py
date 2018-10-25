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
		return redirect(url_for('status')) 
		'''
		except Exception as e:
			return "Database connection error", print(e)
		'''
	return render_template('home.html')


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
        #cur.close()
        #conn.close()

        return render_template("search.html", rows=rows)
    '''
    results = []
    searc_string = request.form['search']
    if search.data['search'] == '':
        qr = conn.query(developers_profile)
        results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/search')
    else:
        #display results
        return render_template('search.html', results=results)
    
    -----------------
    results = []
    search_string = search.data['search']
    if search.data['search'] == '':
        qry = db_session.query(developers_profile)
        results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('search.html', results=results)
    -----------------
    '''

   # query = request.args('search')
# Query table
#for row in conn.execute('SELECT * FROM cafe'):
 #   print(row)

# give connection back to the connection pool
#conn.close()
    



@app.route("/status", methods=['GET', 'POST'])
def status():
	return render_template('status.html')








if __name__ == '__main__':
	app.run(debug=True)