from sqlmodel import create_engine, SQLModel, Session
from settings import get_settings
import os

settings = get_settings()

# Determine which database URL to use based on environment
if os.getenv("APP_ENV") == "LOCAL":
    engine = create_engine(settings.DATABASE_URL, echo=True)
else:
    # For production or other environments, use the configured DATABASE_URL
    engine = create_engine(settings.DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
        
    