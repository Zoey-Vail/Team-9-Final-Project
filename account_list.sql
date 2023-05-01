CREATE TABLE account (
    username VARCHAR(255),
    password VARCHAR(255),
	email    VARCHAR(255),
    age    VARCHAR(255),
    website    VARCHAR(255),
    gender    VARCHAR(255),
    major    VARCHAR(255),
    concentration    VARCHAR(255),
    PRIMARY KEY (username)
);
select username, password, email, age, website, gender, major, concentration
from account;