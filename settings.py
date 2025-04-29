from os import environ
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Environment
    APP_ENV: str = environ.get("APP_ENV", "LOCAL")
    
    # Database configuration
    POSTGRES_USER: str = environ.get("POSTGRES_USER", "admin")
    POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD", "admin")
    POSTGRES_DB: str = environ.get("POSTGRES_DB", "stratum")
    POSTGRES_HOST: str = environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = environ.get("POSTGRES_PORT", "5432")
    
    # Database URL - same format for both environments
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    
    # API configuration
    API_HOST: str = environ.get("API_HOST", "127.0.0.1")
    API_PORT: int = int(environ.get("API_PORT", "8000"))
    
    # Logging configuration
    DEBUG_LOGGING: bool = environ.get("DEBUG_LOGGING", "True").lower() == "true"
    
    # LLM Configuration
    LLM_PROVIDER: str = environ.get("LLM_PROVIDER", "azure")  # "openai" or "azure"
    OPENAI_MODEL: str = environ.get("OPENAI_MODEL", "gpt-4-turbo")
    OPENAI_TEMPERATURE: float = float(environ.get("OPENAI_TEMPERATURE", "0.2"))
    
    # OpenAI configuration
    OPENAI_API_KEY: str = environ.get("OPENAI_API_KEY", "")
    
    # Azure OpenAI Configuration
    AZURE_OPENAI_API_KEY: str = environ.get("AZURE_OPENAI_API_KEY", "")
    AZURE_OPENAI_ENDPOINT: str = environ.get("AZURE_OPENAI_ENDPOINT", "")
    AZURE_OPENAI_DEPLOYMENT_NAME: str = environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini")
    AZURE_OPENAI_API_VERSION: str = environ.get("AZURE_OPENAI_API_VERSION", "2024-08-01-preview")
    
    # SAS to Python conversion settings
    MAX_TOKENS: int = int(environ.get("MAX_TOKENS", "4000"))
    SYSTEM_PROMPT: str = environ.get("SYSTEM_PROMPT", "You are an expert at converting SAS code to Python code. Provide clean, well-documented Python code with appropriate libraries.")
    
    # Rate Limiter Configuration
    RATE_LIMITER_RPS: int = int(environ.get("RATE_LIMITER_RPS", "10"))
    RATE_LIMITER_BUCKET_SIZE: int = int(environ.get("RATE_LIMITER_BUCKET_SIZE", "10"))

def get_settings():
    return Config() 
