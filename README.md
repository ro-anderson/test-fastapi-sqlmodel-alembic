# FastAPI + SQLModel + Alembic Integration Example

This project demonstrates the integration of FastAPI, SQLModel, and Alembic to create a robust API with database management and migration capabilities. It implements a simple music database with bands and albums.

## Technologies

- **FastAPI**: A modern, fast web framework for building APIs with Python
- **SQLModel**: A library for interacting with SQL databases from Python code, with Python objects
- **Alembic**: A database migration tool for SQLAlchemy (which SQLModel is built on)

## Project Structure

```
├── alembic.ini            # Alembic configuration
├── api.http               # HTTP request examples for testing
├── db.py                  # Database connection setup
├── db.sqlite              # SQLite database file
├── main.py                # FastAPI application and endpoints
├── Makefile               # Helper commands for common operations
├── migrations/            # Alembic migrations directory
├── models.py              # Data models using SQLModel
├── pyproject.toml         # Project dependencies
└── README.md              # This file
```

## Data Models

The project implements a music database with the following models:

- **Band**: Represents a music band with a name and genre
- **Album**: Represents an album with a title, release date, and association to a band

## API Endpoints

- `POST /bands`: Create a new band with optional albums
- `GET /bands/{band_id}`: Get a specific band by ID
- `GET /bands`: List all bands with optional filtering by genre and name

## Setup and Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -e .
   ```
3. Initialize the database:
   ```bash
   make alembic-upgrade
   ```

## Running the Application

```bash
# Start the FastAPI server
uvicorn main:app --reload
```

## Testing the API

You can use the provided `api.http` file with a REST client (like VS Code's REST Client extension) to test the API endpoints, or use curl:

```bash
# Create a new band with albums
curl -X POST http://localhost:8000/bands/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Band","genre":"rock","albums":[{"title":"Test Album","release_date":"2024-01-01"}]}'

# Get all bands
curl http://localhost:8000/bands

# Get a specific band
curl http://localhost:8000/bands/1

# Filter bands by genre
curl http://localhost:8000/bands?genre=rock
```

## Database Migrations

The project uses Alembic for database migrations. Common commands are available in the Makefile:

```bash
# Create a new migration
make alembic-revision msg="your migration message"

# Apply migrations
make alembic-upgrade

# View available commands
make help
```

## Learning Resources

This project is based on the following tutorials:

- [FastAPI with SQLModel and Alembic](https://www.youtube.com/watch?v=pRYzMF04fLw) by BugBytes
- [FastAPI SQLModel Tutorial](https://www.youtube.com/watch?v=zTSmvUVbk8M) by BugBytes
