CREATE DATABASE IF NOT EXISTS store;
USE store;


create table user
	(username varchar(20) NOT NULL,
	 userpass varchar(20) NOT NULL,
	 role ENUM('customer','staff') NOT NULL,
	 id int NOT NULL,
	 primary key (username)
	);

create table customer
  ( id INT NOT NULL,
    first_name varchar(20),
    last_name varchar(20),
    balance  numeric(10,2),
    primary key(id)
  );

  create table delivery
  ( id INT NOT NULL,
	cid INT NOT NULL,
    street_num varchar(20),
    street_name varchar(50),
    city varchar(20),
    state varchar(20),
    zip numeric (5,0),
    primary key(id),
    foreign key(cid) references customer(id)
  );

create table staff
	(id	INT NOT NULL,
 	 first_name varchar(20) NOT NULL,
	 last_name  varchar(20) NOT NULL,
	 home_address varchar(100),
	 salary	numeric(7,2),
	 job_title ENUM('cashier', 'manager', 'stocker'),
	 primary key (id)
	);


create table credit_card
  ( id INT NOT NULL,
    cid INT NOT NULL,
    card_num numeric (20,0),
    street_num varchar(20),
    street_name varchar(50),
    city varchar(20),
    state varchar(20),
    zip numeric(5,0),
    primary key(id),
    foreign key(cid) references customer(id)
  );

create table warehouse
	(id		INT NOT NULL,
	 street_num varchar(20),
     street_name varchar(50),
     city varchar(20),
     state varchar(20),
     zip numeric(5,0),
	 storage_capacity numeric(10,0),
	 primary key (id)
	);

create table stock
	(wid		INT NOT NULL,
	 pid		INT NOT NULL,
	 quantity  numeric(7,0),
	 primary key (wid, pid),
     foreign key (wid) references warehouse(id)
	);


create table products
	(id INT NOT NULL,
	 name varchar(20) NOT NULL,
	 type ENUM('food', 'beverage'),
     nutrition_facts varchar(100),
     size numeric(7,2),
	 primary key (id)
	);

create table price
	(id INT NOT NULL,
     pid INT NOT NULL,
	 state varchar(2) NOT NULL,
	 price numeric(7,2) NOT NULL,
	 primary key (id),
     foreign key (pid) references products(id),
     constraint unique_in_state unique(pid, state)
	);

create table orders
	(ccid INT,
	 cid INT NOT NULL,
	 oid INT NOT NULL,
	 pid INT NOT NULL,
	 quantity numeric(7,0),
	 date varchar(30),
	 status ENUM ('issued', 'sent', 'recieved'),
	 primary key (oid, pid),
	 foreign key (cid) references customer(id),
     foreign key (ccid) references credit_card(id),
	 foreign key (pid) references products (id)
	);

create table cart
	(cid INT NOT NULL,
     pid INT NOT NULL,
     quantity numeric(7,0),
	 primary key (pid, cid),
     foreign key (pid) references products (id),
     foreign key (cid) references customer(id)
     );
