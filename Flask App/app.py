from flask import Flask, render_template,request
from flask.ext.mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'sql9.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql9162504'
app.config['MYSQL_PASSWORD'] = 'T6tBGLRX8Q'
app.config['MYSQL_DB'] = 'sql9162504'

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





@app.route('/execute', methods = ['POST','GET'])
def execute():
    return render_template('execute.html')


if __name__=='__main__':
    app.run(debug = True)
