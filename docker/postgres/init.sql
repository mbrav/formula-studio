CREATE USER admin PASSWORD 'admin';

CREATE DATABASE app;

GRANT ALL PRIVILEGES ON DATABASE app TO admin;
FLUSH PRIVILEGES;