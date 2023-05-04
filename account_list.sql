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
CREATE TABLE forums (
	forum_id INT,
    forum_name VARCHAR(255),
    description VARCHAR(255),
    PRIMARY KEY (forum_id)
);
select username, password, email, age, website, gender, major, concentration
from account;

select forum_id, forum_name, description
from forums;
