INSERT INTO Video (videoCode, videoLength) VALUES (123, 120);
INSERT INTO Video (videoCode, videoLength) VALUES (234, 90);
INSERT INTO Video (videoCode, videoLength) VALUES (345, 180);
INSERT INTO Video (videoCode, videoLength) VALUES (456, 240);
INSERT INTO Video (videoCode, videoLength) VALUES (567, 150);

INSERT INTO Model (modelNo, width, height, weight, depth, screenSize) VALUES ('ModelA', 15.25, 12.50, 3.75, 5.00, 21.50);
INSERT INTO Model (modelNo, width, height, weight, depth, screenSize) VALUES ('ModelB', 14.00, 11.75, 4.25, 4.50, 18.75);
INSERT INTO Model (modelNo, width, height, weight, depth, screenSize) VALUES ('ModelC', 16.75, 14.25, 4.00, 5.75, 23.00);
INSERT INTO Model (modelNo, width, height, weight, depth, screenSize) VALUES ('ModelD', 13.50, 11.00, 3.00, 4.15, 19.50);
INSERT INTO Model (modelNo, width, height, weight, depth, screenSize) VALUES ('ModelE', 17.00, 15.00, 5.50, 6.25, 24.50);

INSERT INTO Site (siteCode, type, address, phone) VALUES (1010, 'bar', '123 Office St', '575-555-1212');
INSERT INTO Site (siteCode, type, address, phone) VALUES (2010, 'bar', '456 Industrial Blvd', '575-555-1213');
INSERT INTO Site (siteCode, type, address, phone) VALUES (3010, 'bar', '789 Seller St', '(575-555-1214');
INSERT INTO Site (siteCode, type, address, phone) VALUES (4010, 'restaurant', '321 Storage St', '575-555-1215');
INSERT INTO Site (siteCode, type, address, phone) VALUES (5010, 'restaurant', '555 Distribution Ave', '575-555-1216');

INSERT INTO DigitalDisplay (serialNo, schedulerSystem, modelNo) VALUES ('000001', 'Random', 'ModelA');
INSERT INTO DigitalDisplay (serialNo, schedulerSystem, modelNo) VALUES ('000002', 'Random', 'ModelB');
INSERT INTO DigitalDisplay (serialNo, schedulerSystem, modelNo) VALUES ('000003', 'Smart', 'ModelC');
INSERT INTO DigitalDisplay (serialNo, schedulerSystem, modelNo) VALUES ('000004', 'Smart', 'ModelD');
INSERT INTO DigitalDisplay (serialNo, schedulerSystem, modelNo) VALUES ('000005', 'Virtue', 'ModelE');

INSERT INTO Client (clientId, name, phone, address) VALUES (201, 'Patty OFurniture', '555-1234', '123 Main St.');
INSERT INTO Client (clientId, name, phone, address) VALUES (202, 'Olive Yew', '555-5678', '456 Oak St.');
INSERT INTO Client (clientId, name, phone, address) VALUES (203, 'Aida Bugg', '555-9012', '789 Elm St.');
INSERT INTO Client (clientId, name, phone, address) VALUES (204, 'Teri Dactyl', '555-3456', '321 Maple Ave.');
INSERT INTO Client (clientId, name, phone, address) VALUES (205, 'Peg Legge', '555-7890', '654 Pine St.');

INSERT INTO TechnicalSupport (empId, name, gender) VALUES (101, 'Percy Vere', 'M');
INSERT INTO TechnicalSupport (empId, name, gender) VALUES (102, 'Ty Ayelloribbin', 'F');
INSERT INTO TechnicalSupport (empId, name, gender) VALUES (103, 'Tony Michaels', 'M');
INSERT INTO TechnicalSupport (empId, name, gender) VALUES (104, 'Rose Bush', 'F');
INSERT INTO TechnicalSupport (empId, name, gender) VALUES (105, 'Pat Thettick', 'M');

INSERT INTO Administrator (empId, name, gender) VALUES (101, 'Eileen Sideways', 'M');
INSERT INTO Administrator (empId, name, gender) VALUES (102, 'Rita Book', 'F');
INSERT INTO Administrator (empId, name, gender) VALUES (103, 'Penny Black', 'F');
INSERT INTO Administrator (empId, name, gender) VALUES (104, 'Stan Dupp', 'F');
INSERT INTO Administrator (empId, name, gender) VALUES (105, 'Faye Clether', 'M');

INSERT INTO Salesman (empId, name, gender) VALUES (101, 'Chris Anthemum', 'M');
INSERT INTO Salesman (empId, name, gender) VALUES (102, 'Anne Teak', 'F');
INSERT INTO Salesman (empId, name, gender) VALUES (103, 'Mary Krismass', 'F');
INSERT INTO Salesman (empId, name, gender) VALUES (104, 'Lynne Gwistic', 'F');
INSERT INTO Salesman (empId, name, gender) VALUES (105, 'Ray Sin', 'M');

INSERT INTO AirtimePackage (packageId, class, startDate, lastDate, frequency, videoCode) VALUES (1, 'economy', '2023-03-01', '2023-03-31', 40, 123);
INSERT INTO AirtimePackage (packageId, class, startDate, lastDate, frequency, videoCode) VALUES (2, 'economy', '2023-03-01', '2023-03-31', 60, 234);
INSERT INTO AirtimePackage (packageId, class, startDate, lastDate, frequency, videoCode) VALUES (3, 'whole day', '2023-03-01', '2023-03-31', 80, 345);
INSERT INTO AirtimePackage (packageId, class, startDate, lastDate, frequency, videoCode) VALUES (4, 'whole day', '2023-04-01', '2023-04-30', 100, 456);
INSERT INTO AirtimePackage (packageId, class, startDate, lastDate, frequency, videoCode) VALUES (5, 'golden hours', '2023-04-01', '2023-04-30', 120, 567);

INSERT INTO AdmWorkHours (empId, day, hours) VALUES (101, '2023-02-23', 8.5);
INSERT INTO AdmWorkHours (empId, day, hours) VALUES (102, '2023-02-22', 7.75);
INSERT INTO AdmWorkHours (empId, day, hours) VALUES (103, '2023-02-23', 6.5);
INSERT INTO AdmWorkHours (empId, day, hours) VALUES (104, '2023-02-24', 9.0);
INSERT INTO AdmWorkHours (empId, day, hours) VALUES (105, '2023-02-25', 8.25);

INSERT INTO Broadcasts (videoCode, siteCode) VALUES (123, 1010);
INSERT INTO Broadcasts (videoCode, siteCode) VALUES (234, 2010);
INSERT INTO Broadcasts (videoCode, siteCode) VALUES (345, 3010);
INSERT INTO Broadcasts (videoCode, siteCode) VALUES (456, 4010);
INSERT INTO Broadcasts (videoCode, siteCode) VALUES (567, 5010);

INSERT INTO Administers (empId, siteCode) VALUES (101, 1010);
INSERT INTO Administers (empId, siteCode) VALUES (102, 2010);
INSERT INTO Administers (empId, siteCode) VALUES (103, 3010);
INSERT INTO Administers (empId, siteCode) VALUES (104, 4010);
INSERT INTO Administers (empId, siteCode) VALUES (105, 5010);

INSERT INTO Specializes (empId, modelNo) VALUES (101, 'ModelA');
INSERT INTO Specializes (empId, modelNo) VALUES (102, 'ModelB');
INSERT INTO Specializes (empId, modelNo) VALUES (103, 'ModelC');
INSERT INTO Specializes (empId, modelNo) VALUES (104, 'ModelD');
INSERT INTO Specializes (empId, modelNo) VALUES (105, 'ModelE');

INSERT INTO Purchases (clientId, empId, packageId, commissionRate) VALUES (201, 101, 1, 0.10);
INSERT INTO Purchases (clientId, empId, packageId, commissionRate) VALUES (202, 102, 2, 0.05);
INSERT INTO Purchases (clientId, empId, packageId, commissionRate) VALUES (203, 103, 3, 0.08);
INSERT INTO Purchases (clientId, empId, packageId, commissionRate) VALUES (204, 104, 4, 0.07);
INSERT INTO Purchases (clientId, empId, packageId, commissionRate) VALUES (205, 105, 5, 0.12);

INSERT INTO Locates (serialNo, siteCode) VALUES ('000001', 1010);
INSERT INTO Locates (serialNo, siteCode) VALUES ('000002', 2010);
INSERT INTO Locates (serialNo, siteCode) VALUES ('000003', 3010);
INSERT INTO Locates (serialNo, siteCode) VALUES ('000004', 4010);
INSERT INTO Locates (serialNo, siteCode) VALUES ('000005', 5010);