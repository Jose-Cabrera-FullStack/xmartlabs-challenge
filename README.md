# S3 File Upload Service


## Description
`s3-upload-service` is a Python-based API project built using FastAPI, a high-performance web framework for creating RESTful APIs.

This service implements a mechanism for clients to obtain pre-signed URLs from the backend to upload files directly to Amazon S3, eliminating the need for direct file uploads through the backend. This approach significantly reduces server resource usage and improves system scalability.

The service follows key principles of **Clean Architecture**, **Hexagonal Architecture**, and **SOLID principles** to ensure a robust and flexible design.

## Endpoints

The service provides the following endpoints:

```python
/: Return the Swagger UI documentation.
/presigned-url: Create a pre-signed URL for uploading a file to S3.
/file-status: Update the status of a file after it has been uploaded.
```

## Running the Service

This project includes a Makefile with useful commands to simplify development and operation tasks:

### Start the service

To build and start the service using Docker:

```bash
make run
```

This command will build and start all necessary containers defined in the docker-compose.yml file. The API will be accessible at http://localhost:8000.

### Run tests

To run the test suite:

```bash
make test
```

This executes pytest within the app container to run all tests.

### Database migrations

To create a new migration:

```bash
make add-migration
```

You'll be prompted to enter a name for the migration, which should briefly describe the changes.

To apply all pending migrations:

```bash
make migrate
```

This will run all unapplied migrations to bring your database schema up to date.

### Environment Variables

The service requires several environment variables which should be defined in a `.env` file:

## Project Structure
```bash
Xmartlabs
├─ alembic
│  ├─ alembic.ini
│  ...
├─ alembic.ini
├─ app
│  ├─ database
│  │  ├─ config.py
│  │  ├─ models.py
│  │  └─ __init__.py
│  ├─ domain
│  │  └─ __init__.py
│  ├─ exceptions
│  │  └─ custom_exception.py
│  ├─ infrastructure
│  │  ├─ aws.py
│  │  ├─ s3.py
│  │  └─ __init__.py
│  ├─ main.py
│  ├─ repository
│  │  ├─ file_storage_repository.py
│  │  └─ __init__.py
│  ├─ routers
│  │  └─ restful_endpoints.py
│  ├─ schemas
│  │  ├─ request
│  │  │  ├─ presigned_url_request.py
│  │  │  ├─ update_file_status_request.py
│  │  │  └─ __init__.py
│  │  └─ response
│  │     ├─ presigned_url_response.**py**
│  │     ├─ update_file_status_response.py
│  │     └─ __init__.py
│  ├─ service
│  │  ├─ file_storage.py
│  │  ├─ presigned_url.py
│  │  └─ __init__.py
│  ├─ settings.py
│  ├─ tests
│  │  ├─ ...
│  └─ utils
│     ├─ constants.py
│     └─ tools.py
├─ docker
│  ├─ .dockerignore
│  ├─ docker-compose.yml
│  ├─ Dockerfile.dev
│  ├─ Dockerfile.prod
│  └─ entrypoint.sh
├─ Makefile
├─ pylintrc
├─ pytest.ini
├─ README.md
├─ requirements.txt
├─ scripts
│  ├─ ipython.py
│  └─ __init__.py
└─ setup.cfg

```

## Scaffolding and Architecture

The project follows a well-organized directory structure:

**app**: This directory contains the main app-related code.

**adapter**: Contains files that connect the service with external services from infrastructure.

**database**: Directory that potentially holds code related to database configuration, connections and models.

**domain**: Contains files representing the project's domain logic.

**infrastructure**: Contains files managing the technical infrastructure of the application.

**main.py**: The main app file where the FastApi application is defined and configured.

**schemas**: Contains data schemas used for app incoming requests and outgoing responses.

**service**: Contains files connect the domain with particular uses cases for the app.

**settings.py**: File to store app configuration, such as environment variables, etc.

**tests**: Directory for automated app tests.

**utils**: Contains utility functions or common tools used in the application.

**scripts**: Contains scripts to help with the development process.

**Note**: These articles is based on the following:

- [Hexagonal Architecture](https://douwevandermeij.medium.com/hexagonal-architecture-in-python-7468c2606b63).
- [FastAPI with Ormar, Docker and Traefik](https://testdriven.io/blog/fastapi-docker-traefik/).

**References**: Inspired by [refactoring](https://refactoring.guru/es/design-patterns/), [12factor](https://12factor.net/es/)

