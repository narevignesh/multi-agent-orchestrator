#!/bin/bash

# Navigate to the backend directory and run the tests
cd backend
pytest tests/ > result.log

# Navigate to the orchestrator-sdk directory and run the tests
cd ../orchestrator-sdk/python
pytest ../tests/ > result.log

# Navigate to the frontend directory and run the tests
cd ../../frontend/streamlit_app
pytest ../tests/ > result.log

# Display the results
cat result.log