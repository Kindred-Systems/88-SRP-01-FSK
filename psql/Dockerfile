FROM postgres:15

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=yourpassword
ENV POSTGRES_DB=game_instance

# Copy initialization script
COPY init.sql /docker-entrypoint-initdb.d/
