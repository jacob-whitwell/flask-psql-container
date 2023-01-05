FROM postgres:latest
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB postgres

#FROM library/postgres
ADD ./init/init.sql /docker-entrypoint-initdb.d/