# app_lifespan.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from bert.model_manager import ModelManager
from graph.graph import initialize_neo4j


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize the BERTopic model and Neo4j connection
    ModelManager.initialize_model()
    initialize_neo4j()  # Initialize Neo4j connection

    yield
    # Shutdown logic here (if needed)
