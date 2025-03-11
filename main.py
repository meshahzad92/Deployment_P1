import os
from fastapi import FastAPI
from database import engine
import models
from routers import tasks
import uvicorn

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Task Manager API")

# Include task-related routes
app.include_router(tasks.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API!"}

# Read PORT from environment variables (default to 8000 for local testing)
port = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)
