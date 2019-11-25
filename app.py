from flask import Flask, render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL
from datetime import date,timedelta
import re

app = Flask(__name__)

mysql = MySQL()


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



def todict(tup,schema):
    if isinstance(schema,str):
        schema = schemas[schema]
    if not tup or len(tup) != len(schema):
        return None
    return {schema[i]:tup[i] for i in range(len(schema))}


# takes a tuple and makes it into a string
def tostr(tup,schema):
    string = ""
    for i in range(len(schema)):
        string += str(tup[i]) + " "
    return string

@app.context_processor
def sqlcommands():
    def getstate(id):
        query = "SELECT STATE FROM CUSTOMER JOIN DELIVERY WHERE CUSTOMER.ID = DELIVERY.CID AND CUSTOMER.ID = \"{}\"".format(id)
        cursor.execute(query)
        state = ['state']
        return [todict(tup, state) for tup in cursor.fetchall()]

    def get_customer_addresses_tostr(id):
        query = "SELECT street_num, street_name, city, state, zip FROM delivery WHERE cid = \"{}\"".format(id)
        cursor.execute(query)
        address = ['street_num', 'street_name', 'city', 'state', 'zip']
        return [tostr(tup, address) for tup in cursor.fetchall()]

    def get_customer_addresses_todict(id):
        query = "SELECT * FROM delivery WHERE cid = \"{}\"".format(id)
        cursor.execute(query)
        return [todict(tup, 'delivery') for tup in cursor.fetchall()]

    def get_one_customer_address_todict(id, delivery_id):
        query = "SELECT * FROM delivery WHERE cid = \"{}\" and id = \"{}\"".format(id, delivery_id)
        cursor.execute(query)
        return [todict(tup, 'delivery') for tup in cursor.fetchall()]

    def get_customer_cards_tostr(id):
        query = "SELECT card_num, street_num, street_name, city, state, zip FROM credit_card WHERE cid = \"{}\"".format(id)
        cursor.execute(query)
        card = ['card_num','street_num', 'street_name', 'city', 'state', 'zip']
        return [tostr(tup, card) for tup in cursor.fetchall()]

    def get_customer_cards_todict(id):
        query = "SELECT * FROM credit_card WHERE cid = \"{}\"".format(id)
        cursor.execute(query)
        return [todict(tup, 'credit_card') for tup in cursor.fetchall()]

    def get_one_customer_card_todict(id, card_id):
        query = "SELECT * FROM credit_card WHERE cid = \"{}\" and id = \"{}\"".format(id,card_id)
        cursor.execute(query)
        return [todict(tup, 'credit_card') for tup in cursor.fetchall()]

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
        query = "select products.id, products.name, cart.quantity, price.price from cart join products join price where products.id = cart.pid and products.id = price.id AND cart.cid = \"{}\"".format(id)
        cursor.execute(query)
        cartitem = ['products.id', 'products.name', 'cart.quantity', 'price.price']
        return [todict(tup, cartitem) for tup in cursor.fetchall()]

    #def getaddress


    return dict(getstate=getstate,get_one_customer_card_todict=get_one_customer_card_todict,get_one_customer_address_todict=get_one_customer_address_todict, get_customer_cards_todict=get_customer_cards_todict,get_customer_cards_tostr=get_customer_cards_tostr,get_customer_addresses_todict=get_customer_addresses_todict,get_customer_addresses_tostr=get_customer_addresses_tostr, getproduct=getproduct, get_state_products=get_state_products, getcart=getcart, getcartitem=getcartitem)


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
    '''
    #retrieve warehouse id
    query = "select warehouse.id as WID from warehouse join customer join delivery where warehouse.state = delivery.state and customer.id = delivery.cid and customer.id = \"{}\"".format(user['id'])
    cursor.execute(query)
    customer_wid = cursor.fetchone()[0]
    #delete from stock (need to modify, this is deleting from stock even if quantity of stock in warehouse > 0, so i think we need to add a quantity comparison if ==0 before delete)
    query = "delete from stock where stock.pid = \"{}\" and stock.wid = \"{}\"".format(product_id, customer_wid)
    cursor.execute(query)
    conn.commit()
    #go to orders.html'''
    return render_template('orders.html', user = user)


#delete product from shopping cart
@app.route('/delete_from_cart/<cartitem_id>/<user_id>/<product_quantity>', methods = ['GET'])
def delete_from_cart(cartitem_id, user_id, product_quantity):
    #delete from cart. This removed the selected item from cart entirely, need to re-add item if want to change quantity
    query = "delete from cart where cart.pid = \"{}\"".format(cartitem_id)
    cursor.execute(query)
    conn.commit()
    '''
    #we don't need the next 2 queries if we only update when submitting order
    #retrieve id from warehouse
    query = "select warehouse.id as WID from warehouse join customer join delivery where warehouse.state = delivery.state and customer.id = delivery.cid and customer.id = \"{}\"".format(user['id'])
    cursor.execute(query)
    customer_wid = cursor.fetchone()[0]
    #update stock
    query = "update stock set quantity = quantity + \"{}\" where wid = \"{}\" and pid= \"{}\"".format(product_quantity, customer_wid, cartitem_id)
    cursor.execute(query)
    conn.commit()'''
    return render_template('orders.html', user=user)



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
            return render_template('account.html', user=user)
        elif request.form.get('submit_button') == 'Go To Cart':
            return render_template('orders.html', user=user)
        elif request.form.get('submit_button') == 'Go To Store':
            return render_template('customer.html', user=user)
    return render_template('account.html', user=user)

@app.route('/editaddress/<delivery_id>', methods = ['GET', 'POST'])
def editaddress(delivery_id):
    card_id=0
    return render_template('edit.html', user=user,delivery_id=delivery_id, card_id=card_id)


@app.route('/editcard/<card_id>', methods = ['GET', 'POST'])
def editcard(card_id):
    delivery_id = 0
    return render_template('edit.html', user=user,delivery_id=delivery_id, card_id=card_id)

@app.route('/add_addr/<user_id>', methods = ['GET', 'POST'])
def add_addr(user_id):
    street_num = request.form.get('street_num')
    street_name = request.form.get('street_name')
    city = request.form.get('city')
    state = request.form.get('state')
    zip_code = request.form.get('zip_code')
    #incrementing the delivery id
    query = "select count(*) from delivery"
    cursor.execute(query)
    conn.commit()
    delivery_id = (cursor.fetchone()[0]) + 1
    #insert new delivery address
    query = "insert into delivery(id, cid, street_num, street_name, city, state, zip) values(\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(delivery_id,user['id'], street_num, street_name, city, state, zip_code)
    cursor.execute(query)
    conn.commit()
    return render_template('orders.html', user=user)

@app.route('/add_card/<user_id>', methods = ['GET', 'POST'])
def add_card(user_id):
    card = request.form.get('card')
    street_num = request.form.get('street_num')
    street_name = request.form.get('street_name')
    city = request.form.get('city')
    state = request.form.get('state')
    zip_code = request.form.get('zip_code')
    #incrementing the card id
    query = "select count(*) from credit_card"
    cursor.execute(query)
    conn.commit()
    card_id = (cursor.fetchone()[0]) + 1
    #insert new credit card
    query = "insert into credit_card(id, cid, card_num, street_num, street_name, city, state, zip) values(\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(card_id,user['id'], card, street_num, street_name, city, state, zip_code)
    cursor.execute(query)
    conn.commit()
    return render_template('orders.html', user=user)

@app.route('/submit_order/<cartitem_id>/<user_id>/<product_quantity>', methods = ['GET'])
def submit_order(cartitem_id, user_id, product_quantity):
    # find the warehouse holding the stock
    query = "select warehouse.id as WID from warehouse join customer join delivery where warehouse.state = delivery.state and customer.id = delivery.cid and customer.id = \"{}\"".format(user_id)
    cursor.execute(query)
    customer_wid = cursor.fetchone()[0]

    # update stock
    query = "update stock set quantity = quantity - \"{}\" where wid = \"{}\" and pid = \"{}\"".format(product_quantity, customer_wid, cartitem_id)
    #query = "update stock set quantity = quantity + \"{}\" where wid = \"{}\" and pid= \"{}\"".format(product_quantity,customer_wid,cartitem_id)
    cursor.execute(query)

    # update orders table
    #address = request.form.get('address')
    #what do we do with the delievery address? --> input into delivery tb?
    #card = request.form.get('card')

    #datetime = datetime.date.today()
    #query = "insert into orders(ccid, cid, oid, pid, quantity, date, status) VALUES(1, 1, 2, 1, 5, '2019-11-25', 'recieved')"

    # need query to delete items from cart

    conn.commit()
    return render_template('order_successful.html', user=user)
    
if __name__ == '__main__':
    app.run(debug=True)
