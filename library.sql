CREATE DATABASE LibraryGui;
use LibraryGui;
CREATE TABLE library(
    Member VARCHAR(40) NOT NULL
    ,PRN_No VARCHAR(45)
    ,ID VARCHAR(45)
    ,FirstName VARCHAR(45)
    ,LastName VARCHAR(45)
    ,Address1 VARCHAR(45)
    ,Address2 VARCHAR(45)
    ,Pincode VARCHAR(45)
    ,Mobile VARCHAR(45)
    ,BookId VARCHAR(45)
    ,BookTitle VARCHAR(45)
    ,Author VARCHAR(45)
    ,DateBorrowed VARCHAR(45)
    ,datedue VARCHAR(45)
    ,dayonbook VARCHAR(45)
    ,latereturnfine VARCHAR(45)
    ,dateoverdue VARCHAR(45)
    ,finalprice VARCHAR(45)
    ,PRIMARY KEY (PRN_No,ID)
);

