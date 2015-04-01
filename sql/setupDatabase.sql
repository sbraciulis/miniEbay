CREATE DATABASE miniEbay;
USE miniEbay;

CREATE TABLE accounts(
	name VARCHAR(16) PRIMARY KEY,
	pass VARCHAR(64) NOT NULL,
	salt VARCHAR(64) NOT NULL
);

CREATE TABLE items(
	itemId INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT UNIQUE,
	title VARCHAR(100) NOT NULL,
	description VARCHAR(250),
	category VARCHAR(32) NOT NULL,
	listedBy VARCHAR(16) NOT NULL,
	buyoutPrice DECIMAL(11, 2),
	status VARCHAR(7) DEFAULT 'PENDING' NOT NULL,
	startTime DATETIME NOT NULL,
	endTime DATETIME NOT NULL
);

CREATE TABLE bids(
	accountName VARCHAR(16),
	itemId INTEGER UNSIGNED,
	price DECIMAL(11, 2) NOT NULL,
	bidTime DATETIME NOT NULL,
	PRIMARY KEY(accountName, itemId)
);