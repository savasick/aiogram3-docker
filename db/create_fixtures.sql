CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username varchar(30),
    user_id BIGINT
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    message_text TEXT
);

INSERT INTO users
    (username, user_id)
VALUES
    ('coolname', 1234567890);