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
           'stock':['wid','pid','quantity'],
           'cart':['cid','pid','quantity']
           }


# Take tuple, create dictionary:
def todict(tup,schema): #assumes right arguments
    if isinstance(schema,str): #allows you to give the name of one of the default schemas
        schema = schemas[schema]    #else, we will just use the schema list that you give us!
    if not tup or len(tup) != len(schema): #no tuple, or mismatch with schema
        return None
    return {schema[i]:tup[i] for i in range(len(schema))}

@app.context_processor
def sqlcommands():
    def getstate(id):
        query = "SELECT STATE FROM CUSTOMER JOIN DELIVERY WHERE CUSTOMER.ID = DELIVERY.CID AND CUSTOMER.ID = \"{}\"".format(id)
        cursor.execute(query)
        state = ['state']
        return [todict(tup, state) for tup in cursor.fetchall()]

    # def shoppingcart(id):
    #     state = getstate(id)
    #     query = "SELECT price.pid, name, quantity, price FROM orders JOIN products JOIN price WHERE orders.pid = products.id AND products.id = price.pid AND orders.cid = \"{}\" AND price.state = \"{}\"".format(id, state[0]['state'])
    #     cursor.execute(query)
    #     cartitem = ['price.pid','name','quantity','price.cost']
    #     return [todict(tup, cartitem) for tup in cursor.fetchall()]

    def get_state_products(id, type):
        state = getstate(id)
        if type == 0:
            query = "select products.id, name, nutrition_facts, price from products join stock join warehouse join price where products.id = stock.pid and stock.pid = price.pid and stock.wid = warehouse.id and price.state = warehouse.state and price.state = \"{}\" and products.type = 'food'".format(state[0]['state'])
            #query = "SELECT products.id, name, nutrition_facts, price FROM products JOIN price WHERE products.id = price.pid AND price.state = \"{}\" AND products.type = 'food'".format(state[0]['state'])
        elif type == 1:
            query = "select products.id, name, nutrition_facts, price from products join stock join warehouse join price where products.id = stock.pid and stock.pid = price.pid and stock.wid = warehouse.id and price.state = warehouse.state and price.state = \"{}\" and products.type = 'beverage'".format(state[0]['state'])
            #query = "SELECT products.id, name, nutrition_facts, price FROM products JOIN price WHERE products.id = price.pid AND price.state = \"{}\" AND products.type = 'beverage'".format(state[0]['state'])
        else:
            query = "select products.id, name, nutrition_facts, price from products join stock join warehouse join price where products.id = stock.pid and stock.pid = price.pid and stock.wid = warehouse.id and price.state = warehouse.state and price.state = \"{}\"".format(state[0]['state'])
            #query = "SELECT products.id, name, nutrition_facts, price FROM products JOIN price WHERE products.id = price.pid AND price.state = \"{}\"".format(state[0]['state'])
        cursor.execute(query)
        product = ['products.id', 'name', 'nutrition_facts', 'price']
        return [todict(tup, product) for tup in cursor.fetchall()]

    def getproduct(id, name):
        state = getstate(id)
        query = "select products.id, name, nutrition_facts, price from products join stock join warehouse join price where products.id = stock.pid and stock.pid = price.pid and stock.wid = warehouse.id and price.state = warehouse.state and price.state = \"{}\" and products.name = \"{}\"".format(state[0]['state'], name)
        cursor.execute(query)
        product = ['products.id', 'name', 'nutrition_facts', 'price']
        return [todict(tup, product) for tup in cursor.fetchall()]

    def getcart(id):
        query = "SELECT * from cart"
        #query = "SELECT * from cart JOIN products where products.id = cart.pid AND cart.cid = \"{}\"".format(id)
        #query = "select pid,quantity from cart where cart.cid = \"{}\"".format(id)
        cursor.execute(query)
        cart = ['cid', 'pid', 'quantity']
        return [todict(tup, cart) for tup in cursor.fetchall()]
    def getcartitem(id):
        query = "select products.name, cart.quantity, price.price from cart join products join price where products.id = cart.pid and products.id = price.id AND cart.cid = \"{}\"".format(id)
        cursor.execute(query)
        cartitem = ['products.name', 'cart.quantity', 'price.price']
        return [todict(tup, cartitem) for tup in cursor.fetchall()]

    #def getaddress


    return dict(getstate=getstate, getproduct=getproduct, get_state_products=get_state_products, getcart=getcart, getcartitem=getcartitem)


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

   data = todict(cursor.fetchone(),'user')
   if data:
       global user
       if data['role'] == 'customer':
           query = "SELECT * FROM customer WHERE id = {}".format(data['id'])
           cursor.execute(query)
           user = todict(cursor.fetchone(),'customer')
           return render_template('customer.html', user=user)
       if data['role'] == 'staff':
            query = "SELECT * FROM staff WHERE id = {}".format(data['id'])
            cursor.execute(query)
            user = todict(cursor.fetchone(),'staff')
            return render_template('staff.html', user=user)


   #return "<h1>User:<\h1><\br>{}".format(cursor.fetchone())


@app.route("/request_filtered_list", methods = ['GET', 'POST'])
def request_filtered_list():
    food = request.form.get('food', 0)
    beverages = request.form.get('beverages', 0)
    if food and beverages:
        return render_template('customer.html', user=user, type=2)
    if food and not beverages:
        return render_template('customer.html', user=user, type=0)
    else:
        return render_template('customer.html', user=user, type=1)

@app.route("/request_product", methods = ['GET', 'POST'])
def request_product():
    name = request.form.get('product_name', 0)
    return render_template('customer.html', user=user, name=name)

@app.route('/update_cart/<product_id>', methods = ['GET'])
def update_cart(product_id):
    product_quantity = request.args.get("product_quantity", 0)
    #insert to cart
    query = "insert into cart(cid, pid, quantity) values (\"{}\",\"{}\",\"{}\") on duplicate key update quantity = \"{}\"".format(user['id'], product_id, product_quantity, product_quantity)
    cursor.execute(query)
    conn.commit()
    #retrieve warehouse id
    query = "select warehouse.id as WID from warehouse join customer join delivery where warehouse.state = delivery.state and customer.id = delivery.cid and customer.id = \"{}\"".format(user['id'])
    cursor.execute(query)
    customer_wid = cursor.fetchone()[0]
    #delete from stock
    query = "delete from stock where stock.pid = \"{}\" and stock.wid = \"{}\"".format(product_id, customer_wid)
    cursor.execute(query)
    conn.commit()
    #go to orders.html
    return render_template('orders.html', user = user)

@app.route('/account/', methods = ['GET'])
def account():
    return render_template('account.html', user=user)

# @app.route('/orders/', methods = ['GET'])
# def orders():
#     if request.method == 'GET':
#         #if request.form.get('submit') == 'submit':
#             product_id = request.args.get("product_id",0)
#             product_quantity = request.args.get("product_quantity", 0)
#             user_id=user['id']
#             #query = "INSERT into cart (cid, pid, quantity) VALUES (\"{}\",\"{}\",\"{}\") on duplicate key update quantity = \"{}\"".format(user_id, product_id,product_quantity, product_quantity)
#             query = "INSERT into cart (cid, pid, quantity) VALUES (\"{}\",\"{}\",\"{}\") on duplicate key update quantity = \"{}\"".format(user_id, product_id,product_quantity, product_quantity)
#             cursor.execute(query)

#     return render_template('orders.html', user=user, product_id=product_id, product_quantity=product_quantity )

#test
@app.route('/staff/', methods = ['GET'])
def staff():
    return render_template('staff.html')

@app.route('/warehouse/', methods = ['GET'])
def warehouse():
    return render_template('warehouse.html')

@app.route('/nav', methods = ['GET', 'POST'])
def nav():
    if request.method == 'POST':
        if request.form.get('submit_button') == 'Go To Account':
            return render_template('account.html')
        elif request.form.get('submit_button') == 'Go To Cart':
            return render_template('orders.html', user=user)
    return render_template('account.html')



if __name__ == '__main__':
    app.run(debug=True)
