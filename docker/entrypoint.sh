#!/bin/bash

echo "Waiting for database to be ready..."
until pg_isready -h db -p 5432 -U paracas
do
    echo "Database is not ready - sleeping"
    sleep 2
done
echo "Database is ready!"

# Start the FastAPI application
exec uvicorn app.main:app --host 0.0.0.0 --reload
