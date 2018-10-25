from flask import Flask, render_template, request, flash, url_for
import mysql.connector as mariadb
app = Flask(__name__)
# code to create table
# CREATE TABLE `patients` (
# 	`id` INT(11) NOT NULL AUTO_INCREMENT,
# 	`name` VARCHAR(25) NULL DEFAULT '0',
# 	`time` VARCHAR(25) NULL DEFAULT '0',
# 	`date` VARCHAR(25) NULL DEFAULT '0',
# 	`symptoms` VARCHAR(300) NULL DEFAULT '0',
# 	PRIMARY KEY (`id`)
# )


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/about')
def about():

    return render_template('about.html')


@app.route('/bookings')
def bookings():

    return render_template('bookings.html')


@app.route('/act', methods=['GET', 'POST'])
def act():

    if(request.method == 'POST'):
        try:
            # $variable = $_POST['name_of_select'];
            name = request.form['name']
            mytime = request.form['mytime']
            print(request.form)
            mydate = request.form['mydate']
            symptoms = request.form['symptoms']
            conn = mariadb.connect(user='root', password='root', database='myprojectdb')
            cur = conn.cursor()
            # $query = "INSERT INTO table (field) VALUES ($variable)";
            sql = "INSERT INTO patients(name, booking_time, date_of_birth, symptoms) VALUES('{}', '{}', '{}', '{}')".format(
                name, mytime, mydate, symptoms)
            cur.execute(sql)
            conn.commit()
            msg = "Thanks for Booking Your Data Has Been Stored"
            return render_template('status.html', msg=msg)
        except Exception as e:

            return "Database connection error", print(e)


@app.route('/bookingdetails')
def bookingdetails():
    conn = mariadb.connect(user='root', password='root', database='myprojectdb')
    # connecting to Database
    cur = conn.cursor()
    # query the DB
    cur.execute("SELECT name, booking_time, date_of_birth, symptoms FROM patients")
    # This query is used to fetch The Data from the Database(READ)
    rows = cur.fetchall()

    return render_template('bookingdetails.html', rows=rows)
    # name = request.form['name']
    # mytime = request.form['time']
    # mydate = request.form['date']
    # symptoms = request.form['symptoms']
    # conn = mariadb.connect(user='root', password='root', database='myprojectdb')
    # # connecting to Database
    # cur = conn.cursor()
    # sql = "INSERT INTO patients(name, mytime, mydate, symptoms) VALUES('{}', '{}', '{}', '{}')".format(
    #     name, mytime, mydate, symptoms)
    # cur.execute(sql)
    # conn.commit()
    # msg = "Thanks for booking!!!"
    # flash('You are now registerd and can log in', 'success')
    # return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)