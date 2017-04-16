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

@app.route('/execute/q8', methods = ['POST','GET'])
def q8():
    return render_template('q8.html')



@app.route('/user', methods = ['POST','GET'])
def user():
    return render_template('user.html')


if __name__=='__main__':
    app.run(debug = True)
