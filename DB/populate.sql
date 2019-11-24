/* Populate DB one initial time
	ONLY RUN ONCE
*/

USE store;

/* Populate users */

INSERT INTO user (username,userpass,role,id) VALUES ('lkosmin', 'leah', 'customer', 1);
INSERT INTO user (username,userpass,role,id) VALUES ('jliu', 'joanna', 'customer', 2);
INSERT INTO user (username,userpass,role,id) VALUES ('mlopez', 'manuel', 'customer', 3);
INSERT INTO user (username,userpass,role,id) VALUES ('hpotter', 'harry', 'customer', 4);
INSERT INTO user (username,userpass,role,id) VALUES ('gwashington', 'george', 'customer', 5);
INSERT INTO user (username,userpass,role,id) VALUES ('dkos', 'daniel', 'customer', 6);
INSERT INTO user (username,userpass,role,id) VALUES ('mjackson', 'michael', 'customer', 7);

INSERT INTO user (username,userpass,role,id) VALUES ('schoi', 'sujin', 'staff', 1);
INSERT INTO user (username,userpass,role,id) VALUES ('jredcliffe', 'janet', 'staff', 2);
INSERT INTO user (username,userpass,role,id) VALUES ('mkiss', 'missy', 'staff', 3);
INSERT INTO user (username,userpass,role,id) VALUES ('bpitt', 'brad', 'staff', 4);
INSERT INTO user (username,userpass,role,id) VALUES ('estone', 'emma', 'staff', 5);
INSERT INTO user (username,userpass,role,id) VALUES ('tjefferson', 'thomas', 'staff', 6);

/* Populate customers */

INSERT INTO customer (id,first_name,last_name,balance) VALUES (1,'Leah', 'Kosmin', 200);
INSERT INTO customer (id,first_name,last_name,balance) VALUES (2,'Joanna', 'Liu', 57.31);
INSERT INTO customer (id,first_name,last_name,balance) VALUES (3,'Manuel', 'Lopez', 312);
INSERT INTO customer (id,first_name,last_name,balance) VALUES (4,'Harry', 'Potter', 5);
INSERT INTO customer (id,first_name,last_name,balance) VALUES (5,'George', 'Washington', 1000);
INSERT INTO customer (id,first_name,last_name,balance) VALUES (6,'Daniel', 'Kosmin', 350);
INSERT INTO customer (id,first_name,last_name,balance) VALUES (7,'Michael', 'Jackson', 546);

/*Populate staff members */

INSERT INTO staff (id,first_name,last_name,home_address,salary,job_title) VALUES (1,'Sujin', 'Choi', '14 South Pin Oak Ave., OK 73072', 45000, 'cashier');
INSERT INTO staff (id,first_name,last_name,home_address,salary,job_title) VALUES (2,'Janet', 'Redcliffe', '94 W. Thatcher St., SC 29464', 85000, 'manager');
INSERT INTO staff (id,first_name,last_name,home_address,salary,job_title) VALUES (3,'Missy', 'Kiss', '9991 Gregory Court, CA 95008', 67000, 'stocker');
INSERT INTO staff (id,first_name,last_name,home_address,salary,job_title) VALUES (4,'Brad', 'Pitt', '9041 Newbridge Avenue, PA 15010', 56000, 'cashier');
INSERT INTO staff (id,first_name,last_name,home_address,salary,job_title) VALUES (5,'Emma', 'Stone', '9022 Liberty Rd., MI 48322', 35000, 'stocker');
INSERT INTO staff (id,first_name,last_name,home_address,salary,job_title) VALUES (6,'Thomas', 'Jefferson', '463 Manchester Ave., MN 55016', 77000, 'manager');


/* Populate Delivery Address */
INSERT INTO delivery (id, cid,street_num,street_name,city,state,zip) VALUES (1, 1, 8265, 'Pierce Lane Pomana','Saginaw', 'CA', 91768);
INSERT INTO delivery (id, cid,street_num,street_name,city,state,zip) VALUES (2, 2, 9871, 'Homestead Ave.Winter','Middleton', 'FL', 32708);
INSERT INTO delivery (id, cid,street_num,street_name,city,state,zip) VALUES (3, 3, 899, 'Woodland LaneBrooklyn','Florence', 'NY', 11201);
INSERT INTO delivery (id, cid,street_num,street_name,city,state,zip) VALUES (4, 4, 7601, 'West Smoky Hollow Ave.','Loxahatchee','NY', 12901);
INSERT INTO delivery (id, cid,street_num,street_name,city,state,zip) VALUES (5, 5, 73, 'Prince St. Alpharetta', 'Springboro','GA', 30004);
INSERT INTO delivery (id, cid,street_num,street_name,city,state,zip) VALUES (6, 6, 893, 'High Ridge St.', 'Belleville','FL', 34786);
INSERT INTO delivery (id, cid,street_num,street_name,city,state,zip) VALUES (7, 7, 595, 'Lake View Road', 'Malden','OH', 44870);

/* Populate credit_card w/ Billing Address */
INSERT INTO credit_card (id,cid,card_num,street_num,street_name,city,state,zip) VALUES (1,1, 4646975990999612, 8265, 'Pierce Lane Pomana','New Haven', 'CA', 91768);
INSERT INTO credit_card (id,cid,card_num,street_num,street_name,city,state,zip) VALUES (2,1, 4287176299413066, 809, 'Surrey StreetTemple Hills','Waterbury', 'MD', 20748);
INSERT INTO credit_card (id,cid,card_num,street_num,street_name,city,state,zip) VALUES (3,2, 4785313887191781, 9871, 'Homestead Ave.Winter','Cornelius', 'FL', 32708);
INSERT INTO credit_card (id,cid,card_num,street_num,street_name,city,state,zip) VALUES (4,3, 4082565824415074, 899, 'Woodland LaneBrooklyn', 'Herndon','NY', 11201);
INSERT INTO credit_card (id,cid,card_num,street_num,street_name,city,state,zip) VALUES (5,3, 4291626340087032, 7564, 'Spring St.New Philadelphia', 'Ridgefield','OH', 44663);
INSERT INTO credit_card (id,cid,card_num,street_num,street_name,city,state,zip) VALUES (6,4, 4496362919882693, 7601, 'West Smoky Hollow Ave.','Uniontown','NY', 12901);
INSERT INTO credit_card (id,cid,card_num,street_num,street_name,city,state,zip) VALUES (7,5, 4627254693560078, 802, 'State Street','Beckley','DE', 19701);
INSERT INTO credit_card (id,cid,card_num,street_num,street_name,city,state,zip) VALUES (8,6, 4762371312660231, 893, 'High Ridge St.', 'Columbus','FL', 34786);
INSERT INTO credit_card (id,cid,card_num,street_num,street_name,city,state,zip) VALUES (9,7, 4086247839350887, 589, 'Sheffield Lane Vernon Hills','Camas', 'IL', 60061);
INSERT INTO credit_card (id,cid,card_num,street_num,street_name,city,state,zip) VALUES (10,7, 4086243439380887, 3421, 'Wabash Lane Vernon Hills','Jaun', 'IN', 60456);


/* Populate Products */
INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (1,'banana','food','Calories:100, Total Fat:0.4g, Polyunsaturated fat: 0.1g',4);
INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (2,'apple','food', 'Calories:130, Total Fat:0.7g, Polyunsaturated fat: 0.8g',7);
INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (3,'chicken','food', 'Calories:400, Total Fat:1.2g, Polyunsaturated fat: 1.4g',25);
INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (4,'hamburger','food', 'Calories:255, Total Fat:4.5, Polyunsaturated fat: 0.8g',7);
INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (5,'beef','food', 'Calories:130, Total Fat:0.8g, Polyunsaturated fat: 0.8g',9);
INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (6,'orange','food', 'Calories:1607, Total Fat:1.2g, Polyunsaturated fat: 0.8g',2);
INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (7,'lettuce','food','Calories:1000, Total Fat:7.2g, Polyunsaturated fat: 0.8g',4 );
INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (8,'broccoli','food', 'Calories:265, Total Fat:0.4g, Polyunsaturated fat: 0.8g',1);
INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (9,'tomato','food', 'Calories:706, Total Fat:1.1g, Polyunsaturated fat: 0.8g',6);


INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (10,'wine','beverage', 'Calories:39, Total Fat:0.2g, Polyunsaturated fat:0g, Total Carbohydrate:9g',6);
INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (11,'pepsi','beverage', 'Calories:40, Total Fat:1.2g, Polyunsaturated fat:5g, Total Carbohydrate:7g',3);
INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (12,'orange juice','beverage', 'Calories:130, Total Fat:2.2g, Polyunsaturated fat:0.1g, Total Carbohydrate:9g',12);
INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (13,'water','beverage', 'Calories:260, Total Fat:3.2g, Polyunsaturated fat:6g, Total Carbohydrate:1g',5);
INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (14,'vitamin water','beverage', 'Calories:30, Total Fat:9.2g, Polyunsaturated fat:3.4g, Total Carbohydrate:2g',9);
INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (15,'beer','beverage', 'Calories:27, Total Fat:7.2g, Polyunsaturated fat:2.3g, Total Carbohydrate:9g',54);
INSERT INTO products (id,name,type, nutrition_facts,size) VALUES (16,'craberry juice','beverage', 'Calories:500, Total Fat:0.3g, Polyunsaturated fat:7g, Total Carbohydrate:10g',6);

/* Populate Food */
/*
INSERT INTO food (pid,nutrition_facts) VALUES (1, 'Calories:100, Total Fat:0.4g, Polyunsaturated fat: 0.1g');
INSERT INTO food (pid,nutrition_facts) VALUES (2, 'Calories:130, Total Fat:0.7g, Polyunsaturated fat: 0.8g');
INSERT INTO food (pid,nutrition_facts) VALUES (3, 'Calories:400, Total Fat:1.2g, Polyunsaturated fat: 1.4g');
INSERT INTO food (pid,nutrition_facts) VALUES (4, 'Calories:255, Total Fat:4.5, Polyunsaturated fat: 0.8g');
INSERT INTO food (pid,nutrition_facts) VALUES (5, 'Calories:130, Total Fat:0.8g, Polyunsaturated fat: 0.8g');
INSERT INTO food (pid,nutrition_facts) VALUES (6, 'Calories:1607, Total Fat:1.2g, Polyunsaturated fat: 0.8g');
INSERT INTO food (pid,nutrition_facts) VALUES (7, 'Calories:1000, Total Fat:7.2g, Polyunsaturated fat: 0.8g');
INSERT INTO food (pid,nutrition_facts) VALUES (8, 'Calories:265, Total Fat:0.4g, Polyunsaturated fat: 0.8g');
INSERT INTO food (pid,nutrition_facts) VALUES (9, 'Calories:706, Total Fat:1.1g, Polyunsaturated fat: 0.8g');

/* Populate Beverage. We don't every need to sort by nutrition info. Just type. So nutrition info can be generic. */
/*
INSERT INTO beverage (pid,nutrition_facts) VALUES (10, 'Calories:39, Total Fat:0.2g, Polyunsaturated fat:0g, Total Carbohydrate:9g');
INSERT INTO beverage (pid,nutrition_facts) VALUES (11, 'Calories:40, Total Fat:1.2g, Polyunsaturated fat:5g, Total Carbohydrate:7g');
INSERT INTO beverage (pid,nutrition_facts) VALUES (12, 'Calories:130, Total Fat:2.2g, Polyunsaturated fat:0.1g, Total Carbohydrate:9g');
INSERT INTO beverage (pid,nutrition_facts) VALUES (13, 'Calories:260, Total Fat:3.2g, Polyunsaturated fat:6g, Total Carbohydrate:1g');
INSERT INTO beverage (pid,nutrition_facts) VALUES (14, 'Calories:30, Total Fat:9.2g, Polyunsaturated fat:3.4g, Total Carbohydrate:2g');
INSERT INTO beverage (pid,nutrition_facts) VALUES (15, 'Calories:27, Total Fat:7.2g, Polyunsaturated fat:2.3g, Total Carbohydrate:9g');
INSERT INTO beverage (pid,nutrition_facts) VALUES (16, 'Calories:500, Total Fat:0.3g, Polyunsaturated fat:7g, Total Carbohydrate:10g');
*/


/* Populate Orders */
INSERT INTO orders (ccid,cid,oid,pid,quantity,date,status) VALUES (1,1,1,16,2,'2016-11-24','recieved');
INSERT INTO orders (ccid,cid,oid,pid,quantity,date,status) VALUES (1,1,1,7,3,'2016-11-24','recieved');
INSERT INTO orders (ccid,cid,oid,pid,quantity,date,status) VALUES (3,3,2,4,10,'2019-09-24','issued');
INSERT INTO orders (ccid,cid,oid,pid,quantity,date,status) VALUES (3,3,2,7,1,'2019-09-24','issued');
INSERT INTO orders (ccid,cid,oid,pid,quantity,date,status) VALUES (5,4,3,10,5,'2013-09-24','sent');
INSERT INTO orders (ccid,cid,oid,pid,quantity,date,status) VALUES (6,6,4,1,4,'2019-01-12','recieved');
INSERT INTO orders (ccid,cid,oid,pid,quantity,date,status) VALUES (6,5,4,15,2,'2019-01-13','recieved');
INSERT INTO orders (ccid,cid,oid,pid,quantity,date,status) VALUES (6,5,6,1,5,'2019-01-13','recieved');
INSERT INTO orders (ccid,cid,oid,pid,quantity,date,status) VALUES (9,7,3,5,7,'2019-05-05','issued');
INSERT INTO orders (ccid,cid,oid,pid,quantity,date,status) VALUES (10,7,2,2,1,'2019-05-05','issued');


/*Populate prices */
INSERT INTO price (id,pid,state,price) VALUES (1, 1, 'OH', 0.50);
INSERT INTO price (id,pid,state,price) VALUES (2, 1, 'IL', 1.00);
INSERT INTO price (id,pid,state,price) VALUES (3, 1, 'CA', 2.00);
INSERT INTO price (id,pid,state,price) VALUES (4, 2, 'CO', 5.00);
INSERT INTO price (id,pid,state,price) VALUES (5, 2, 'NY', 6.04);
INSERT INTO price (id,pid,state,price) VALUES (6, 3, 'OR', 0.75);
INSERT INTO price (id,pid,state,price) VALUES (7, 4, 'AL', 2.99);
INSERT INTO price (id,pid,state,price) VALUES (8, 4, 'OH', 3.15);
INSERT INTO price (id,pid,state,price) VALUES (9, 4, 'IN', 2.66);
INSERT INTO price (id,pid,state,price) VALUES (10, 4, 'IA', 2.00);
INSERT INTO price (id,pid,state,price) VALUES (11, 5,'KY', 1.50);
INSERT INTO price (id,pid,state,price) VALUES (12, 5, 'MS', 2.99);
INSERT INTO price (id,pid,state,price) VALUES (13, 5, 'IN', 0.75);
INSERT INTO price (id,pid,state,price) VALUES (14, 6, 'OH', 3.99);
INSERT INTO price (id,pid,state,price) VALUES (15, 6, 'IL', 2.10);
INSERT INTO price (id,pid,state,price) VALUES (16, 6, 'ID', 1.99);
INSERT INTO price (id,pid,state,price) VALUES (17, 6, 'FL', 3.05);
INSERT INTO price (id,pid,state,price) VALUES (18, 7, 'GA', 2.35);
INSERT INTO price (id,pid,state,price) VALUES (19, 7, 'WA', 1.99);
INSERT INTO price (id,pid,state,price) VALUES (20, 8, 'DE', 3.15);
INSERT INTO price (id,pid,state,price) VALUES (21, 9, 'CT', 2.50);
INSERT INTO price (id,pid,state,price) VALUES (22, 9, 'AZ', 1.75);
INSERT INTO price (id,pid,state,price) VALUES (23, 10, 'PA', 8.00);
INSERT INTO price (id,pid,state,price) VALUES (24, 10, 'HI', 7.65);
INSERT INTO price (id,pid,state,price) VALUES (25, 10, 'IN', 6.30);
INSERT INTO price (id,pid,state,price) VALUES (26, 10, 'KS', 5.65);
INSERT INTO price (id,pid,state,price) VALUES (27, 11, 'MA', 3.45);
INSERT INTO price (id,pid,state,price) VALUES (28, 11, 'OH', 5.45);
INSERT INTO price (id,pid,state,price) VALUES (29, 11, 'GA', 6.00);
INSERT INTO price (id,pid,state,price) VALUES (30, 12, 'FL', 34.00);
INSERT INTO price (id,pid,state,price) VALUES (31, 12, 'OR', 27.00);
INSERT INTO price (id,pid,state,price) VALUES (32, 12, 'WA', 15.00);
INSERT INTO price (id,pid,state,price) VALUES (33, 13, 'CO', 16.30);
INSERT INTO price (id,pid,state,price) VALUES (34, 13, 'OH', 7.55);
INSERT INTO price (id,pid,state,price) VALUES (35, 13, 'AL', 10.30);
INSERT INTO price (id,pid,state,price) VALUES (36, 13, 'AZ', 1.30);
INSERT INTO price (id,pid,state,price) VALUES (37, 14, 'IL', 4.50);
INSERT INTO price (id,pid,state,price) VALUES (38, 14, 'HI', 7.60);
INSERT INTO price (id,pid,state,price) VALUES (39, 14, 'LA', 4.99);
INSERT INTO price (id,pid,state,price) VALUES (40, 15, 'FL', 3.34);
INSERT INTO price (id,pid,state,price) VALUES (41, 16, 'ME', 1.75);
INSERT INTO price (id,pid,state,price) VALUES (42, 16, 'ID', 3.60);
INSERT INTO price (id,pid,state,price) VALUES (43, 16, 'CT', 2.50);
INSERT INTO price (id,pid,state,price) VALUES (44, 4, 'NY', 5.00);


/*Populate warehouse*/
INSERT INTO warehouse (id,street_num,street_name,city,state,zip,storage_capacity) VALUES (1, 7924, 'Wintergreen Rd.', 'Medford', 'MA', 02155, 560);
INSERT INTO warehouse (id,street_num,street_name,city,state,zip,storage_capacity) VALUES (2, 467, 'Winding Way Rd.', 'Jonesborough', 'TN', 37659, 200);
INSERT INTO warehouse (id,street_num,street_name,city,state,zip,storage_capacity) VALUES (3, 8091, 'Brickell Court', 'Wilson', 'IL', 27893, 145);
INSERT INTO warehouse (id,street_num,street_name,city,state,zip,storage_capacity) VALUES (4, 590, 'Orchard St.','Elizabeth City', 'NY', 27909, 435);
INSERT INTO warehouse (id,street_num,street_name,city,state,zip,storage_capacity) VALUES (5, 19, 'Ridgeview Ave.','Bloomington', 'IN', 47401, 45);
INSERT INTO warehouse (id,street_num,street_name,city,state,zip,storage_capacity) VALUES (6, 8390, 'Center Road','Minot', 'IL', 58701, 160);
INSERT INTO warehouse (id,street_num,street_name,city,state,zip,storage_capacity) VALUES (7, 8442, 'Vernon Street','Twin Falls', 'ID', 83301, 99);
INSERT INTO warehouse (id,street_num,street_name,city,state,zip,storage_capacity) VALUES (8, 346, 'Bridgeton Dr.','Milford', 'OH',01757, 300);


/*populate stock*/
INSERT INTO stock (wid,pid,quantity) VALUES (1,1,400);
INSERT INTO stock (wid,pid,quantity) VALUES (1,2,300);
INSERT INTO stock (wid,pid,quantity) VALUES (1,7,350);
INSERT INTO stock (wid,pid,quantity) VALUES (2,3,70);
INSERT INTO stock (wid,pid,quantity) VALUES (2,10,99);
INSERT INTO stock (wid,pid,quantity) VALUES (2,9,199);
INSERT INTO stock (wid,pid,quantity) VALUES (3,8,400);
INSERT INTO stock (wid,pid,quantity) VALUES (3,5,200);
INSERT INTO stock (wid,pid,quantity) VALUES (4,4,400);
INSERT INTO stock (wid,pid,quantity) VALUES (5,1,300);
INSERT INTO stock (wid,pid,quantity) VALUES (5,3,200);
INSERT INTO stock (wid,pid,quantity) VALUES (6,11,400);
INSERT INTO stock (wid,pid,quantity) VALUES (7,13,600);





