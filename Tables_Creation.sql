DROP TABLE IF EXISTS Subsidiary CASCADE;
DROP TABLE IF EXISTS Restaurant CASCADE;
DROP TABLE IF EXISTS Warehouse CASCADE;
DROP TABLE IF EXISTS Delivers CASCADE;
DROP TABLE IF EXISTS Supplier CASCADE;
DROP TABLE IF EXISTS Supply CASCADE;
DROP TABLE IF EXISTS SupplierContact CASCADE;
DROP TABLE IF EXISTS Managers CASCADE;
DROP TABLE IF EXISTS ManagerContact CASCADE;
DROP TABLE IF EXISTS Staff CASCADE;
DROP TABLE IF EXISTS StaffContact CASCADE;

CREATE TABLE Subsidiary (
   subsidiaryID INT PRIMARY KEY,
   subsidiaryName VARCHAR(100),
   subsidiaryLocation VARCHAR(100),
   subsidiaryExec VARCHAR(100),
   execSalary INT check (execSalary > 0)
   );

CREATE TABLE Managers (
   managerID INT PRIMARY KEY,
   managerName VARCHAR(100),
   managerRole VARCHAR(100)
   );

CREATE TABLE ManagerContact (
   managerID INT,
   managerContact VARCHAR(50),
   PRIMARY KEY (managerID, managerContact),
   FOREIGN KEY (managerID) REFERENCES Managers(managerID)
   );

CREATE TABLE Restaurant (
   restaurantID INT PRIMARY KEY,
   restaurantName VARCHAR(100),
   restaurantLocation VARCHAR(100),
   restaurantType VARCHAR(50),
   openingDate DATE,
   subsidiaryID INT,
   managerID INT,
   FOREIGN KEY (subsidiaryID) REFERENCES Subsidiary(subsidiaryID),
   FOREIGN KEY (managerID) REFERENCES Managers(managerID)
   );

CREATE TABLE Warehouse (
   warehouseID INT PRIMARY KEY,
   warehouseLocation VARCHAR(100),
   warehouseItems VARCHAR(100),
   warehouseQty INT Check (warehouseQty >= 0)
   );

CREATE TABLE Delivers (
   restaurantID INT,
   warehouseID INT,
   PRIMARY KEY (restaurantID, warehouseID),
   FOREIGN KEY (restaurantID) REFERENCES Restaurant(restaurantID),
   FOREIGN KEY (warehouseID) REFERENCES Warehouse(warehouseID)
   );

CREATE TABLE Supplier (
   supplierID INT PRIMARY KEY,
   supplierName VARCHAR(100),
   supplierRep VARCHAR(100)
   );

CREATE TABLE SupplierContact (
   supplierID INT,
   supplierContact VARCHAR(50),
   PRIMARY KEY (supplierID, supplierContact),
   FOREIGN KEY (supplierID) REFERENCES Supplier(supplierID)
   );

CREATE Table Supply(
   supplierID INT,
   warehouseID INT,
   PRIMARY KEY (supplierID, warehouseID),
   FOREIGN KEY (supplierID) REFERENCES Supplier(supplierID),
   FOREIGN KEY (warehouseID) REFERENCES Warehouse(warehouseID)
   );

CREATE TABLE Staff (
   staffID INT PRIMARY KEY,
   staffName VARCHAR(100),
   staffRole VARCHAR(50),
   restaurantID INT,
   managerID INT,
   FOREIGN KEY (restaurantID) REFERENCES Restaurant(restaurantID),
   FOREIGN KEY (managerID) REFERENCES Managers(managerID)
   );

CREATE TABLE StaffContact (
   staffID INT,
   staffContact VARCHAR(50),
   PRIMARY KEY (staffID, staffContact),
   FOREIGN KEY (staffID) REFERENCES Staff(staffID)
   );