import os
DB_URL = os.getenv("DB_URL", "postgresql+psycopg2://user:password@localhost:5432/realesate_db")
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")
APP_ENV = os.getenv("APP_ENV", "dev")
