from flask import Flask, render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL
from datetime import date,timedelta
import re

app = Flask(__name__)

# Intialize MySQL
mysql = MySQL()


# database connection details below
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pass'
app.config['MYSQL_DATABASE_DB'] = 'store'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

app = Flask(__name__)

user = None


schemas = {'user': ['username', 'userpass', 'role', 'id'],
           'customer':['id','first_name','last_name','balance'],
           'staff':['id','first_name','last_name','home_address','salary','job_title'],
           'delivery':['id', 'cid','street_num','street_name','city','state','zip'],
           'credit_card':['id','cid','card_num','street_num','street_name','city','state','zip'],
           'products':['id','name','type', 'nutrition_facts','size'],
           'orders':['ccid','cid','oid','pid','quantity','date','status'],
           'price':['id','pid','state','price'],
           'warehouse':['id','street_num','street_name','city','state','zip','storage_capacity'],
           'stock':['wid','pid','quantity']
           }

# Take tuple, create dictionary:
def tup2dict(tup,schema): #assumes right arguments
    if isinstance(schema,str): #allows you to give the name of one of the default schemas
        schema = schemas[schema]    #else, we will just use the schema list that you give us!
    if not tup or len(tup) != len(schema): #no tuple, or mismatch with schema
        return None
    return {schema[i]:tup[i] for i in range(len(schema))}



@app.route("/")
def index():
    return render_template('login.html')

@app.route('/login',methods = ['POST'])
def login():
   username = request.form['username']
   password = request.form['password']
   query = "SELECT * FROM user WHERE username = \"{}\" AND userpass = \"{}\"".format(username, password)
   cursor.execute(query)

   #data = tup2dict(cursor.fetchone(),'user')
   #if data:
   #    global user
   #    if data['role'] == 'customer':


   return "<h1>User:<\h1><\br>{}".format(cursor.fetchone())



if __name__ == '__main__':
    app.run(debug=True)



