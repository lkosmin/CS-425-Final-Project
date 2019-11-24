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

@app.context_processor
def sqlcommands():
    def getstate(id):
        query = "SELECT STATE FROM CUSTOMER NATURAL JOIN DELIVERY WHERE CUSTOMER.ID = DELIVERY.CID AND CUSTOMER.ID = \"{}\"".format(id)
        cursor.execute(query)
        state = ['state']
        return [tup2dict(tup, state) for tup in cursor.fetchall()] 

    def shoppingcart(id):
        query = "SELECT pid, name, quantity, price FROM orders JOIN products JOIN price WHERE orders.pid = products.id AND orders.cid = \"{}\"".format(id)
        cursor.execute(query)
        cartitem = ['pid','name','quantity','cost']
        return [tup2dict(tup, cartitem) for tup in cursor.fetchall()]

    def getproducts(id):
        state = getstate(id)
        query = "SELECT products.id, name, nutrition_facts, price FROM products JOIN price WHERE products.id = price.pid AND price.state = \"{}\"".format(state[0]['state'])
        cursor.execute(query)
        product = ['products.id', 'name', 'nutrition_facts', 'price']
        return [tup2dict(tup, product) for tup in cursor.fetchall()]
    
    #def getaddress


    return dict(getstate=getstate, shoppingcart=shoppingcart,getproducts=getproducts)


###



@app.route("/")
def index():
    return render_template('login.html')

@app.route('/home',methods = ['POST'])
def login():
   username = request.form['username']
   password = request.form['password']
   query = "SELECT * FROM user WHERE username = \"{}\" AND userpass = \"{}\"".format(username, password)
   cursor.execute(query)

   data = tup2dict(cursor.fetchone(),'user')
   if data:
       #global user
       if data['role'] == 'customer':
           query = "SELECT * FROM customer WHERE id = {}".format(data['id'])
           cursor.execute(query)
           user = tup2dict(cursor.fetchone(),'customer')
           return render_template('customer.html', user=user)
       if data['role'] == 'staff':
            query = "SELECT * FROM staff WHERE id = {}".format(data['id'])
            cursor.execute(query)
            user = tup2dict(cursor.fetchone(),'staff')
            return render_template('staff.html', user=user)


   #return "<h1>User:<\h1><\br>{}".format(cursor.fetchone())

@app.route('/customer', methods = ['GET', 'POST'])
def customer():
    return render_template('customer.html')

@app.route('/account/', methods = ['GET'])
def account():
    return render_template('account.html', user=user)

@app.route('/orders/', methods = ['GET'])
def orders():
    return render_template('orders.html')

#test
@app.route('/staff/', methods = ['GET'])
def staff():
    return render_template('staff.html')

@app.route('/warehouse/', methods = ['GET'])
def warehouse():
    return render_template('warehouse.html')


if __name__ == '__main__':
    app.run(debug=True)
