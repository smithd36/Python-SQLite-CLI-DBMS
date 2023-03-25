PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
CREATE TABLE Video (videoCode integer primary key, videoLength integer);
CREATE TABLE Model (modelNo char(10) primary key, width numeric(6,2), height numeric (6,2), weight numeric (6,2), depth numeric (6,2), screenSize numeric(6,2));
CREATE TABLE Site (siteCode integer primary key, type varchar (16) check (type IN ('bar', 'restaurant')), address varchar(100), phone varchar(16));
CREATE TABLE DigitalDisplay (serialNo char(10) primary key, schedulerSystem char(10) check (schedulerSystem IN ('Random', 'Smart', 'Virtue')), modelNo char(10), Foreign key (modelNo) references Model (modelNo));
CREATE TABLE Client (clientId integer primary key, name varchar(40), phone varchar(16), address varchar(100));
CREATE TABLE TechnicalSupport (empId integer primary key, name varchar(40), gender char(1));
CREATE TABLE Administrator (empId integer primary key, name varchar(40), gender char(1));
CREATE TABLE Salesman (empId integer primary key, name varchar(40), gender char(1));
CREATE TABLE AirtimePackage (packageId integer primary key, class varchar(16) check (class IN ('economy', 'whole day', 'golden hours')), startDate date, lastDate date, frequency integer, videoCode integer);
CREATE TABLE AdmWorkHours (empId integer not null, day date not null, hours numeric (4,2), primary key(empId, day), foreign key (empId) references Administrator (empId));
CREATE TABLE Broadcasts (videoCode integer not null, siteCode integer not null, primary key (videoCode, siteCode), foreign key(videoCode) references Video (videoCode), foreign key (siteCode) references Site (siteCode));
CREATE TABLE Administers (empId integer not null, siteCode integer not null, primary key(empId, siteCode), foreign key (empId) references TechnicalSupport (empId), foreign key (siteCode) references Site (siteCode));
CREATE TABLE Specializes (empId integer not null, modelNo char(10) not null, primary key (empId, modelNo), foreign key (empId) references TechnicalSupport (empId), foreign key (modelNo) references Model (ModelNo));
CREATE TABLE Purchases (clientId integer not null, empId integer not null, packageId integer not null, commissionRate numeric(4,2), primary key (clientId, empId, packageId), foreign key (clientId) references Client (clientId), foreign key (empId) references Salesman (empId), foreign key (packageId) references Airtimepackage (packageId));
CREATE TABLE Locates (serialNo char(10) not null, siteCode integer not null, primary key(serialNo, siteCode), foreign key (serialNo) references DigitalDisplay (serialNo), foreign key (siteCode) references Site (siteCode));
COMMIT;