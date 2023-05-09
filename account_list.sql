CREATE TABLE account (
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
	email    VARCHAR(255) NOT NULL,
    age    VARCHAR(255) NOT NULL,
    website    VARCHAR(255),
    gender    VARCHAR(255),
    major    VARCHAR(255) NOT NULL,
    concentration    VARCHAR(255) NOT NULL,
    logged_In   boolean NOT NULL,
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
    parent_forum_name VARCHAR(255),
	title VARCHAR(255),
    content VARCHAR(1000),
    tags VARCHAR(255),
    majors VARCHAR(255),
    classes VARCHAR(255),
    companies VARCHAR(255),
    PRIMARY Key (discuss_ID)
);
CREATE TABLE comment (
    comment_ID INT,
    reply_content VARCHAR(1000),
    parent_discussion_ID INT,
    creator_username VARCHAR(255),
    PRIMARY Key (comment_ID)
);
select username, password, email, age, website, gender, major, concentration, logged_In
from account;

select forum_id, forum_name, description
from forums;

select discuss_ID, title, content, creator_username, parent_forum_ID
from discussion;
