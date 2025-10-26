#!/bin/bash

# Navigate to the frontend directory
cd frontend/streamlit_app

# Install the required packages
pip install -r ../requirements.txt

# Start the Streamlit application
streamlit run app.py --server.port 8501 --server.address 0.0.0.0