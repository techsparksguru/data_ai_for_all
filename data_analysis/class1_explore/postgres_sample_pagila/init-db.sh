#!/bin/bash
set -e

echo 'Importing data into db $POSTGRES_DB'
psql --username $POSTGRES_USER -d $POSTGRES_DB < /docker-entrypoint-initdb.d/pagila-schema.sql
echo 'Importing insert-data finished successfully'
psql --username $POSTGRES_USER -d $POSTGRES_DB < /docker-entrypoint-initdb.d/pagila-data.sql
echo 'Importing data finished successfully'

echo 'Data import finished successfully'