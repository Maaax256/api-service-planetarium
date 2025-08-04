# Planetarium API

A Django REST API service for planetarium management,  
enabling users to browse astronomy shows, explore show themes,   
view planetarium domes with seating capacity, and book specific  
seats for show sessions. The system supports secure JWT  
authentication, user reservation history, and comprehensive  
admin controls for managing shows, themes, domes, sessions,  
and reservations. Interactive API documentation is provided via  
Swagger and ReDoc. Built with Docker, Django REST Framework,  
and PostgreSQL for robust, scalable deployment.

## Features

- Creating, deleting and updating astronomy shows, themes,  
  planetarium domes and show sessions for admin users;
- Viewing lists and retrieving - for all users;
- Reserving tickets on astronomy show sessions;
- JWT authentication and authorization;
- API documentation with Swagger and ReDoc;
- Admin resource for system management;

## Tech Stack

- Docker & Docker Compose
- Django REST Framework
- PostgreSQL 14-alpine
- Python 3.13 (3.13-slim in Docker)
- Git

## Quick Start

### 1. Clone the repository

```bash
    git clone https://github.com/Maaax256/api-service-planetarium.git
    
    cd api-service-planetarium
```

### 2. Configure environment variables
    
Create .env file and copy variables from .env.sample to .env

### 3. Build and start the services

```bash
    # To build and start containers
    docker-compose up --build

    # To run in detached mode (background)
    docker-compose up -d

    # To stop the containers
    docker-compose down
```

### 4. Fill database with fake data

```bash
    docker-compose exec app python manage.py fake_db_data
```

### 5. Create superuser

```bash
    docker-compose exec app python manage.py createsuperuser
```

### 6. Access the API

- ReDoc: http://localhost:8080/api/doc/redoc/
- Swagger: http://localhost:8080/api/doc/swagger/

    
