CREATE TABLE jurl (
                id integer PRIMARY KEY,
                shortURL TEXT UNIQUE NOT NULL,
                targetURL TEXT NOT NULL
            );
