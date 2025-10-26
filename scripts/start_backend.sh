#!/bin/bash

# Navigate to the backend directory
cd backend/app

# Start the FastAPI application
uvicorn main:app --host 0.0.0.0 --port 8000 --reload