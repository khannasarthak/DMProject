from flask import Flask, render_template,request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sarthak'
app.config['MYSQL_PASSWORD'] = 'qwerty123'
app.config['MYSQL_DB'] = 'dbms_projectphase3'

mysql = MySQL(app)

@app.route('/',methods = ['POST','GET'])
def index():
    return render_template('index.html',  )

@app.route('/process', methods=['POST'])
def process():
    query = request.form['query']
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    colNames = [i[0] for i in cursor.description]
    return render_template('execute.html', dbstuff = data, columns= colNames, query = query)

@app.route('/q3', methods=['POST']) # viewtop 10
def pq3():
    num = request.form['query']
    query = 'SELECT customer_name, COUNT(booking.customer_id) FROM booking, customer WHERE  booking.customer_id = customer.customer_id GROUP BY booking.customer_id ORDER BY COUNT(booking.booking_id) DESC LIMIT ' + num
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    colNames = [i[0] for i in cursor.description]
    return render_template('q3.html', dbstuff = data, columns= colNames, query = query)

@app.route('/pq1', methods=['POST']) # add event
def pq1():
    cursor = mysql.connection.cursor()
    showid = request.form['showid']
    showid = '"'+showid+'"'
    etime = request.form['etime']
    etime = '"'+etime+'"'
    edate = request.form['edate']
    edate = '"'+edate+'"'
    tprice = request.form['tprice']
    # query = 'SET @show_id='+showid+';SET @time_event ="'+etime+'";set @date_event = "'+edate+'";set @ticket_price = "'+tprice+'";insert into eventtable(show_id,time_event,date_event,ticket_price) values(@show_id,@time_event,@date_event,@ticket_price);'
    query = 'INSERT into eventtable(show_id,time_event,date_event,ticket_price) values('+showid+','+etime+','+edate+','+tprice+');'
    cursor.execute(query)
    print ('++++++++++++++++ce')
    mysql.connection.commit()
    return render_template('q1d.html', query = query)

@app.route('/q2', methods=['POST']) # Option for admin to add event

def pq2():
    showname = request.form['query']
    showname = '"%'+showname+'%"'
    query = 'SELECT show_name, COUNT(reservation.show_id) AS num_of_reservations FROM	shows JOIN 	reservation ON reservation.show_id = shows.show_id  WHERE show_name like '+showname+' GROUP BY reservation.show_id '
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    colNames = [i[0] for i in cursor.description]
    return render_template('q2.html', dbstuff = data, columns= colNames, query = query)

@app.route('/q4', methods=['POST']) # Number of movies released in the year selected by the admin
def pq4():
    year = request.form['year']
    print (year)
    query = 'SELECT release_date, COUNT(shows.show_id) AS Total_movie FROM shows JOIN movie ON movie.show_id = shows.show_id WHERE release_date ='+year+' GROUP BY release_date'
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    colNames = [i[0] for i in cursor.description]
    return render_template('q4.html', dbstuff = data, columns= colNames, query = query)

@app.route('/q5', methods=['POST']) # viewtop 10
def pq5():
    showname = request.form['query']
    showname = '"%'+showname+'%"'
    query = 'SELECT e_id, ticket_price FROM eventtable WHERE 	eventtable.show_id in (SELECT  shows.show_id FROM shows	WHERE 	show_name like '+showname+')'
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    colNames = [i[0] for i in cursor.description]
    return render_template('q5.html', dbstuff = data, columns= colNames, query = query)

@app.route('/q6', methods=['POST']) # viewtop 10
def pq6():
    ptype = request.form['query']
    ptype = '"%'+ptype+'%"'
    num = request.form['num']
    query = 'SELECT	performance.show_id, performers, show_name FROM	performance, shows WHERE	performance_type like '+ptype+' 	AND shows.show_id = performance.show_id LIMIT '+ num
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    colNames = [i[0] for i in cursor.description]
    return render_template('q6.html', dbstuff = data, columns= colNames, query = query)

@app.route('/q7', methods=['POST']) # viewtop 10
def pq7():
    eid = request.form['query']
    eid = '"'+eid+'"'

    query = 'SELECT	COUNT(booking_id) FROM	booking WHERE 	e_id = '+ eid+ ' GROUP BY e_id'
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    colNames = [i[0] for i in cursor.description]
    return render_template('q7.html', dbstuff = data, columns= colNames, query = query)

@app.route('/q8', methods=['POST']) # viewtop 10
def pq8():
    numt = request.form['query']
    numt = '"'+numt+'"'
    num = request.form['num']
    query = 'SELECT customer_name FROM	(SELECT    customer_id, COUNT(booking.num_tickets) 	FROM    	booking	GROUP BY booking.customer_id	HAVING COUNT(booking.num_tickets) = '+numt+ ') AS s,	customer WHERE 	s.customer_id = customer.customer_id LIMIT '+num
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    colNames = [i[0] for i in cursor.description]
    return render_template('q8.html', dbstuff = data, columns= colNames, query = query)

@app.route('/q9', methods=['POST']) # viewtop 10
def pq9():
    eid = request.form['query']
    eid = '"'+eid+'"'

    query = 'SELECT	hall.name_hall FROM	hall WHERE hall.hall_id IN (SELECT reservation.hall_id FROM reservation WHERE reservation.show_id IN (SELECT show_id FROM eventtable WHERE e_id ='+eid+'))'
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    colNames = [i[0] for i in cursor.description]
    return render_template('q9.html', dbstuff = data, columns= colNames, query = query)

@app.route('/q10', methods=['POST']) # viewtop 10
def pq10():
    showid = request.form['query']
    showid = '"'+showid+'"'

    query = 'SELECT	show_name, reservation.r_date, reservation.r_time FROM reservation JOIN shows ON reservation.show_id = shows.show_id WHERE	reservation.show_id = '+showid
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    colNames = [i[0] for i in cursor.description]
    return render_template('q10.html', dbstuff = data, columns= colNames, query = query)




@app.route('/execute', methods = ['POST','GET'])
def execute():
    return render_template('execute.html')

@app.route('/execute/q3', methods = ['POST','GET'])
def q3():
    return render_template('q3.html')

@app.route('/execute/q2', methods = ['POST','GET'])
def q2():
    return render_template('q2.html')

@app.route('/execute/q1', methods = ['POST','GET'])
def q1():
    return render_template('q1.html')

@app.route('/execute/q4', methods = ['POST','GET'])
def q4():
    return render_template('q4.html')

@app.route('/execute/q5', methods = ['POST','GET'])
def q5():
    return render_template('q5.html')

@app.route('/execute/q6', methods = ['POST','GET'])
def q6():
    return render_template('q6.html')

@app.route('/execute/q7', methods = ['POST','GET'])
def q7():
    return render_template('q7.html')

@app.route('/execute/q9', methods = ['POST','GET'])
def q9():
    return render_template('q9.html')

@app.route('/execute/q10', methods = ['POST','GET'])
def q10():
    return render_template('q10.html')

@app.route('/execute/q11', methods = ['POST','GET'])
def q11():
    return render_template('q11.html')

@app.route('/execute/q12', methods = ['POST','GET'])
def q12():
    return render_template('q12.html')

@app.route('/execute/q8', methods = ['POST','GET'])
def q8():
    return render_template('q8.html')



@app.route('/user', methods = ['POST','GET'])
def user():
    return render_template('user.html')


if __name__=='__main__':
    app.run(debug = True)
