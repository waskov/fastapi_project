-- create database
CREATE DATABASE mydatabase;

-- connect
\c mydatabase;

-- create table
CREATE TABLE mytable (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT
);

-- insert into table
INSERT INTO mytable (name, age) VALUES ('John', 25);
INSERT INTO mytable (name, age) VALUES ('Jane', 30);
