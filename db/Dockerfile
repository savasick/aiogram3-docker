FROM postgres:latest

#ENV POSTGRES_PASSWORD=$BOT_DATABASE_PASSWORD
#ENV POSTGRES_USER=$BOT_DATABASE_USER
#ENV POSTGRES_DB=$BOT_DATABASE_NAME
#ENV POSTGRES_HOST=$BOT_DATABASE_HOST

COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql