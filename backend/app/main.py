from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.config import CORS_ORIGINS, APP_ENV

app = FastAPI(title="Simple Housing Prediction API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[CORS_ORIGINS, "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok", "environment": APP_ENV}

