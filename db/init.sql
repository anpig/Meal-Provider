CREATE TABLE Staff_Information(
    StaffID BIGINT PRIMARY KEY,
    StaffName VARCHAR(255),
    Position VARCHAR(255),
    Gmail VARCHAR(255),
    Password VARCHAR(255),
    PhoneNumber BIGINT
);
INSERT INTO Staff_Information (StaffID, StaffName, Position, Gmail, Password, PhoneNumber) VALUES 
    (100001, 'ycy.yo', 'restaurant', 'ycy.yo@gmail.com', 'test', 0909090909), 
    (100002, 'amber chen', 'admin', 'hello@world', 'test', 0910101010),
    (100003, 'whoami', 'worker', 'who@ami', 'test', 0911111111);