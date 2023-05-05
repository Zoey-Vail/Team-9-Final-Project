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
CREATE TABLE discussion (
    discuss_ID INT,
    creator_username VARCHAR(255),
    parent_forum_ID INT,
	title VARCHAR(255),
    content VARCHAR(1000),
    tags VARCHAR(255),
    majors VARCHAR(255),
    classes VARCHAR(255),
    companies VARCHAR(255),
    PRIMARY Key (discuss_ID)
);
select username, password, email, age, website, gender, major, concentration
from account;

select forum_id, forum_name, description
from forums;
