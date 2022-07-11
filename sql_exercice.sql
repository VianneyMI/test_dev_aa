/*
Setting up a dummy  database for the exercice

Used https://sqliteonline.com/ to make some tests

Disclaimers :
- I haven't wrote SQL queries in more than a year
- I used to use ORMs such as SQLAlchemy to avoid having to write SQL queries myself when I had to
*/

CREATE TABLE Brands
(
    id INTEGER PRIMARY KEY,
    name NVARCHAR(255) NOT NULL
);

INSERT INTO Brands (id, name) VALUES (1, 'Peugeot'), (2, 'Opel'), (3, 'Citroen'), (4, 'ds'), (5, 'Mercedes');

CREATE TABLE Cars(
    id INTEGER PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    brand_id INTEGER NOT NULL,
    modele NVARCHAR(255) NOT NULL,
    doors INTEGER NOT NULL,
    color NVARCHAR(255) NOT NULL,
    price INTEGER NOT NULL,
    FOREIGN KEY (brand_id) REFERENCES Brands(id)
);


INSERT INTO Cars(id, name, brand_id, modele, doors, color, price) VALUES
(1, 'Peugeot', 1, '208', 5, 'blanc', 15000),
(2, 'Opel', 2, 'Astra', 5, 'rouge', 12000),
(3, 'Citroen', 3, 'C4', 5, 'bleu', 9000),
(4, 'ds', 4, 'ds', 5, 'blanc', 5000),
(5, 'Mercedes', 5, 'C class', 5, 'rouge', 20000);

CREATE TABLE Clients(
    id INTEGER PRIMARY KEY,
    mail NVARCHAR(255) NOT NULL,

);

INSERT INTO Clients(id, mail) VALUES
(1, 'test@test.fr'),
(2, 'dummy@dummy.com'),
(3, 'example@example.edu'),
(4, 'mock@mock.io');


CREATE TABLE Orders(
    id INTEGER PRIMARY KEY,
    car_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    total_price INTEGER NOT NULL,
    status NVARCHAR(255) NOT NULL,
    FOREIGN KEY (car_id) REFERENCES Cars(id),
    FOREIGN KEY (client_id) REFERENCES Clients(id)
);

INSERT INTO Orders(id, car_id, client_id, total_price, status) VALUES
(1, 1, 1, 15000, 'paid'),
(2, 2, 2, 12000, 'paid'),
(3, 3, 3, 9000, 'paid'),
(4, 4, 4, 5000, 'paid'),
(5, 5, 4, 20000, 'paid');

CREATE TABLE Payments(
    id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    type NVARCHAR(255) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(id)
);

INSERT INTO Payments(id, order_id, amount, type, date) VALUES
(1, 1, 15000, 'cash'),
(2, 2, 12000, 'cash'),
(3, 3, 9000, 'cb'),
(4, 4, 5000, 'cb'),
(5, 4, 10000, 'cheque'),
(6, 4, 5000, 'virement')

/*Answering the questions*/

/*Question 1*/
SELECT * FROM Orders LEFT JOIN Cars on Orders.car_id=Cars.id LEFT JOIN Brands ON Brands.id = Cars.brand_id
	WHERE Brands.name = 'Peugeot' OR Brands.name = 'Opel' OR Brands.name = 'ds' OR Brands.name = 'Citroen';

/*Question 2*/
SELECT * FROM Orders LEFT JOIN Cars on Orders.car_id=Cars.id
	WHERE Cars.price > 10000 ;

/*Question 3*/
SELECT COUNT('id') as nb_payment_type, Payments.type AS payment_type
FROM Payments LEFT JOIN Orders ON Payments.order_id = Orders.id
WHERE Orders.status = 'accepted'
GROUP BY Payments.type, Orders.status;

/*Question 4*/
SELECT * FROM Orders LEFT JOIN Cars ON Orders.car_id=Cars.id LEFT JOIN Brands ON Cars.brand_id = Brands.id LEFT JOIN Payments ON Orders.id = Payments.order_id
WHERE Orders.status = 'accepted' AND Brands.name = 'dacia' AND Cars.doors = 5
/*Incomplete would need to use subqueries to handle the payments constraint. Skipped for sake of time*/

/*Question 5*/
SELECT * FROM Clients LEFT JOIN Orders ON Orders.client_id = Clients.id LEFT JOIN Cars on Cars.id = Orders.car_id
WHERE LEFT(LOWER(Clients.mail),1)='d' AND Cars.color='rouge' and Orders.status='accepted';