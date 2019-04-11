#!/usr/bin/env bash

psql -U postgres << EOF

    DROP DATABASE IF EXISTS canairio;
    CREATE DATABASE canairio
        WITH
        OWNER = postgres
        ENCODING = 'UTF8'
        LC_COLLATE = 'C'
        LC_CTYPE = 'C'
        TABLESPACE = pg_default
        CONNECTION LIMIT = -1;

    GRANT ALL ON DATABASE canairio TO postgres;

    GRANT TEMPORARY, CONNECT ON DATABASE canairio TO PUBLIC;

    GRANT ALL ON DATABASE canairio TO canairio_user;
EOF

./manage.py migrate
