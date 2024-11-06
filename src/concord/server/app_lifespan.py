# app_lifespan.py
from contextlib import asynccontextmanager
from fastapi import FastAPI

from bert.model_manager import ModelManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize the BERTopic model
    ModelManager.initialize_model()
    yield
    # Shutdown: Perform any necessary cleanup here
