---
layout: page
toc: true
title: SQL Basics
lab: 1
---

~~~~sql

/*
This SQL tutorial is specific to SQLite, and can be run from https://sqliteonline.com/
*/
------------------------CREATE TABLE AND ADD DATA----------------------------------------

--This command will create a Table with the following specs.
CREATE TABLE CustomerInfo
( 
  id int PRIMARY KEY AUTOINCREMENT,        --PRIMARY KEY will be unique to each row. AUTOINCREMENT will increase the id value by 1 for each row
  first_name varchar(50),    --first_name is the name of the column. varchar(50) says that it can have up to 50 characters
  last_name varchar(50),
  age int                    --age is an integer
  )

--Lets add another column called city
ALTER TABLE CustomerInfo ADD city varchar(50);

-- Insert some values into table
INSERT INTO CustomerInfo (first_name, last_name, age, city) values ('Alfred', 'Ampersand', 34, 'Albuquerque');
INSERT INTO CustomerInfo (first_name, last_name, age, city) values ('Barbara', 'Betsy', 33, 'Boston');
INSERT INTO CustomerInfo (first_name, last_name, age, city) values ('Colin', 'Campbell', 22, 'Cincinatti');
INSERT INTO CustomerInfo (first_name, last_name, age, city) values ('Dorothy', 'Dartsmouth', 47, 'Denver');
INSERT INTO CustomerInfo (first_name, last_name, age, city) values ('Edmond', 'Darth', 34, 'Denver');
INSERT INTO CustomerInfo (first_name, last_name, age, city) values ('Edmond', 'Eagleson', 37, 'Denver');
INSERT INTO CustomerInfo (first_name, last_name, age, city) values ('Frederick', 'Dart', 34, 'Denver');
INSERT INTO CustomerInfo (first_name, last_name, age, city) values ('George', 'Gregory', 34, 'Denver');

------------------------VIEW DATA IN TABLE----------------------------------------
-- Now make sure that you've added them correctly. Select different portions of the table
SELECT * FROM CustomerInfo --select everything from the table
SELECT first_name, last_name FROM CustomerInfo --select the columns first_name and last_name for every row in the table
SELECT * FROM CustomerInfo WHERE first_name= 'Edmond'; -- select every column for rows where the first_name is 'Edmond'
Select * FROM CustomerInfo WHERE first_name= 'Edmond' AND last_name = 'Darth';
Select * FROM CustomerInfo  WHERE last_name LIKE 'Dart%'; -- % matches nothing or anything
Select * FROM CustomerInfo  WHERE last_name LIKE 'Dart_%'; -- _ matches 1 character


-------------------------FURTHER OPERATIONS----------------------------------------


UPDATE CustomerInfo SET Age=23, last_name='Appleton' WHERE first_name='Alfred';

DELETE FROM CustomerInfo WHERE first_name='Alfred'; --Delete row from table

DROP Customer; //Drop (Delete) the table;


-----------------MORE COMPLEX STUFF TO BE LOOKED AT LATER-------------------------------




CREATE TABLE Customer
(
    Id int Primary Key identity(1,1),
    [First Name] varchar(50),
    LastName varchar(50),
    Age int,
    City varchar(50)
)

CREATE TABLE CustomerInfo
( 
  id int PRIMARY KEY,
  first_name varchar(50),
  last_name varchar(50),
  age int,
  )

--insert records again

CREATE TABLE Products
(
    id int primary key identity(1,1)
    ProductName varchar(50)
)

ALTER TABLE Products ADD Price float;

INSERT INTO Products (ProductName, Price) values ('Baseball', 5.95);
INSERT INTO Products (ProductName, Price) values ('Bat', 195.99);


CREATE TABLE Orders
(
    OrderID int primary key identity(1,1),
    OrderDate Datetime,
    CustomerID int,
    ProductID int
)

SELECT * FROM Orders

SELECT * FROM Products;
SELECT * FROM Customer;

INSERT INTO Orders (OrderDate, CustomerID, ProductID) values (GetDate(), 2, 2);
INSERT INTO Orders (OrderDate, CustomerID, ProductID) values (GetDate(), 1, 1);
INSERT INTO Orders (OrderDate, CustomerID, ProductID) values (GetDate(), 2, 2);
INSERT INTO Orders (OrderDate, CustomerID, ProductID) values (GetDate(), 1, 1);
INSERT INTO Orders (OrderDate, CustomerID, ProductID) values (GetDate(), 3, 2);
INSERT INTO Orders (OrderDate, CustomerID, ProductID) values (GetDate(), 3, 1);

ALTER TABLE Orders ADD FOREIGN KEY (CustomerID) references Customer(ID)

DELETE Orders WHERE OrderID=21;

ALTER TABLE Orders ADD FOREIGN KEY (ProductID) references Products(ID)

SELECT * FROM Orders
INNER JOIN Products ON Orders.ProductID=Products.ID;

SELECT * FROM Orders as o
INNER JOIN Products as p ON o.ProductID=p.ID;

SELECT * FROM Orders o
INNER JOIN Products p ON o.ProductID=p.ID;

SELECT o.*,p.*, c.* FROM Orders o
INNER JOIN Products p ON o.ProductID=p.ID INNER JOIN Customer c on o.CustomerID=c.ID;

SELECT o.OrderDate,p.ProductName,p.Price, c.* FROM Orders o
INNER JOIN Products p ON o.ProductID=p.ID INNER JOIN Customer c on o.CustomerID=c.ID;


functions and group bys

SELECT sum(p.Price) Total
INNER JOIN Products p ON o.ProductID=p.ID INNER JOIN Customer c on o.CustomerID=c.ID;



SELECT c.LastName, sum(p.Price) Total
INNER JOIN Products p ON o.ProductID=p.ID INNER JOIN Customer c on o.CustomerID=c.ID group by c.LastName;

SELECT c.LastName,p.ProductName, sum(p.Price) Total
INNER JOIN Products p ON o.ProductID=p.ID INNER JOIN Customer c on o.CustomerID=c.ID group by c.LastName, p.ProductName;

SELECT c.City, sum(p.Price) Total, AVG(p.price) Average
INNER JOIN Products p ON o.ProductID=p.ID INNER JOIN Customer c on o.CustomerID=c.ID group by c.City;

Indexes

person

primary key person_id
first_name
last_name
birthday

SELECT COUNT(*) FROM person;

SELECT COUNT(*) FROM person WHERE last_name = 'Smith';

SELECT COUNT(*) FROM person WHERE first_name = 'Emma';

SELECT COUNT(*) FROM person WHERE birthday BETWEEN date1 and date2

SELECT COUNT(*) FROM person WHERE last_name in ('Hawkins', 'Snow');

CREATE INDEX person_first_name_idx ON person (first_name); (Reduces speed taken from 4000ms to 500 ms)

CREATE INDEX person_first_name_last_name_idx ON person (last_name, first_name); //order matters. This will sort by last name and then by first name

UNION ALL - Joins results from top to bottom (including duplicates)
UNION - Joins results from top to bottom (deleting duplicates)

~~~~



* Primary keys do not reference other tables.
* Foreign keys reference other tables.
* Learn about Indexes!!

