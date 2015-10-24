CREATE TABLE Events
(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Name VARCHAR(255),
Location VARCHAR(255),
City VARCHAR(255),
Description VARCHAR(255),
Organiser VARCHAR(255),
Time INTEGER,
#interest VARCHAR(225)
);


CREATE TABLE Interests
(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
InterestID VARCHAR(255),
EventID VARCHAR(255)
);

#For each(interest in i)
#SELECT * FROM Events WHERE interest LIKE '%$i%'