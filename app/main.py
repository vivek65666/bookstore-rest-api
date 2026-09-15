from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bookstore REST API",
    description="""
    A REST API for managing bookstore inventory.

    Features:
    - Create, read, update, and delete books
    - Search books by title or author
    - SQLite database integration
    - Input validation and error handling
    """,
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Bookstore REST API"
    }