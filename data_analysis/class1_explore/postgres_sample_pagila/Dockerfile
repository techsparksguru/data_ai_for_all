FROM postgres:9.6.3-alpine

ENV POSTGRES_DB pagila
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres

COPY *.sh /docker-entrypoint-initdb.d/
COPY *.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
CMD ["postgres"]