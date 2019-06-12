#!/bin/bash
set -ex

POSTGRES="psql --username ${POSTGRES_USER}"

echo "Creating database: ${POSTGRES_DB}"
echo "Creating database: ${POSTGRES_TEST_DB}"

$POSTGRES <<EOSQL
CREATE DATABASE "${POSTGRES_DB}" OWNER "${POSTGRES_USER}";
CREATE DATABASE "${POSTGRES_TEST_DB}" OWNER "${POSTGRES_USER}";
EOSQL
