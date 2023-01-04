-- Create the database and credentials
CREATE USER docker;
CREATE DATABASE docker;
GRANT USAGE ON SCHEMA public TO docker;
GRANT ALL PRIVILEGES ON DATABASE docker TO docker;

-- Connect to the docker database before creating the table
\c docker

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(30) NOT NULL,
    lastname VARCHAR(30) NOT NULL
);

INSERT INTO users VALUES (1, 'jay', 'whitwell'),
(2, 'destina', 'bartley'),
(3, 'huthayfa', 'patel');