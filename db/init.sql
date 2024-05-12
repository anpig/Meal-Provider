CREATE TABLE Staff_Info (
    StaffID BIGINT PRIMARY KEY,
    StaffName VARCHAR(255),
    Position VARCHAR(255),
    Gmail VARCHAR(255),
    Password VARCHAR(255),
    PhoneNumber VARCHAR(20)
);
INSERT INTO Staff_Info (StaffID, StaffName, Position, Gmail, Password, PhoneNumber) VALUES 
    (100001, 'ycy.yo', 'restaurant', 'ycy.yo@gmail.com', 'test', '0909090909'), 
    (100002, 'amber chen', 'admin', 'hello@world', 'test', '0910101010'),
    (100003, 'whoami', 'worker', 'who@ami', 'test', '0911111111'),
    (100004, 'benson', 'worker', 'benson@gmail.com', 'test', '0912345678'),
    (100005, 'detaomega', 'worker', 'detaomega@gmail.com', 'test', '0912345678'),
    (100006, 'BruceLin', 'worker', 'bruce@gmail.com', 'test', '0943134344');

CREATE TABLE Dish_Info(
    DishID BIGINT PRIMARY KEY AUTO_INCREMENT,
    RestaurantID BIGINT,
    Name VARCHAR(255),
    Description VARCHAR(1000),
    Picture VARCHAR(255),
    Price INT,
    Available BOOLEAN,
    TimesOfOrder INT,
    Rating FLOAT
);

INSERT INTO Dish_Info (RestaurantID, Name, Description, Picture, Price, Available, TimesOfOrder, Rating) VALUES
    (1, "Fried Chicken", "Delicious", "chicken.jpg", 200, TRUE, 0, 4.5),
    (1, "Hamburger", "Delicious", "chicken.jpg", 150, TRUE, 0, 4.5),
    (1, "French Fries", "Delicious", "chicken.jpg", 100, TRUE, 0, 4.5),
    (2, "Cookie", "Delicious", "chicken.jpg", 30, TRUE, 0, 4.5),
    (2, "Veggie Delite", "Delicious", "chicken.jpg", 150, FALSE, 0, 4.5),
    (2, "Tuna", "Delicious", "chicken.jpg", 170, TRUE, 0, 4.5),
    (3, "Pepperoni Pizza", "Delicious", "chicken.jpg", 200, TRUE, 0, 4.5),
    (3, "Hawaiian Pizza", "Delicious", "chicken.jpg", 150, TRUE, 0, 4.5),
    (3, "Cheese Pizza", "Delicious", "chicken.jpg", 100, FALSE, 0, 4.5);

CREATE TABLE Restaurant_Info (
    RestaurantID BIGINT PRIMARY KEY AUTO_INCREMENT,
    RestaurantName VARCHAR(255),
    PhoneNumber VARCHAR(20),
    OpenTime TIME,
    CloseTime TIME,
    Description VARCHAR(1000),
    Picture VARCHAR(255),
    Rating FLOAT
);

INSERT INTO Restaurant_Info  (RestaurantName, PhoneNumber, OpenTime, CloseTime, Description, Picture, Rating) VALUES 
    ('KFC', '0912345678', '12:00:00', '22:00:00', 'Fast Food Restaurant', 'kfc.png', 4.3),
    ('Subway', '0912345678', '08:00:00', '22:00:00', 'Sandwich', 'kfc.png', 5.0),
    ('Pizza Hut', '0912345678', '08:00:00', '22:00:00', 'Pizza', 'kfc.png', 3.9);


CREATE TABLE Order_Dish( -- time to take the meal?
    SerialID BIGINT PRIMARY KEY AUTO_INCREMENT,
    OrderID BIGINT,
    DishID BIGINT
);

INSERT INTO Order_Dish (OrderID, DishID) VALUES
    (1, 1),
    (1, 2),
    (2, 5),
    (3, 7),
    (3, 8);

CREATE TABLE Orders (
    OrderID BIGINT PRIMARY KEY AUTO_INCREMENT,
    CustomerID BIGINT,
    RestaurantID BIGINT,
    TotalPrice INT,
    OrderTime TIMESTAMP,
    onAccount BOOLEAN
);

INSERT INTO Orders (CustomerID, RestaurantID, TotalPrice, OrderTime, onAccount) VALUES
    (100003, 1, 350, '2021-06-01 14:00:00', FALSE),
    (100006, 2, 150, '2021-06-01 12:00:00', TRUE),
    (100005, 3, 350, '2021-06-01 20:00:00', TRUE);
