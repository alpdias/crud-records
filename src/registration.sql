-- table creation and its columns

CREATE TABLE registration (
    id INT(3) NOT NULL AUTO_INCREMENT,
    company VARCHAR(30) NOT NULL,
    register VARCHAR(13) NOT NULL,
    tax VARCHAR(6) DEFAULT NULL,
    email VARCHAR(30) DEFAULT NULL,
    telephone VARCHAR(12) DEFAULT NULL,
    office VARCHAR(30) DEFAULT NULL,
    situation VARCHAR(8) DEFAULT 'inactive',
    PRIMARY KEY (id)
);

-- list of companies to use as an example

INSERT INTO registration VALUES 
(1,'Google','P000000312312','income','google@google.com','511-452-3425','California','active'),
(2,'Apple','L000000312312','sales','apple@apple.com','455-444-1312','California','inactive'),
(3,'Amazon','P000000123432','income','amazon@amazon.com','321-656-8675','Texas','active'),
(4,'walmart','C000000456987','sales','walmart@walmart.com','345-123-0000','Chicago','active');
