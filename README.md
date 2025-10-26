# Multi-Agent Orchestrator

## Overview
The Multi-Agent Orchestrator is a system designed to manage and coordinate multiple AI agents, enabling them to work together efficiently. This project utilizes FastAPI for the backend and Streamlit for the frontend, providing a robust framework for building and interacting with AI-driven applications.

## Project Structure
```
multi-agent-orchestrator
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── api
│   │   │   └── v1
│   │   │       ├── routes.py
│   │   │       └── deps.py
│   │   ├── agents
│   │   │   ├── base.py
│   │   │   ├── manager.py
│   │   │   └── orchestrator.py
│   │   ├── services
│   │   │   ├── llm_client.py
│   │   │   ├── retriever.py
│   │   │   └── memory.py
│   │   ├── models
│   │   │   └── schemas.py
│   │   ├── core
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   └── utils
│   │       └── logging.py
│   ├── tests
│   │   ├── test_routes.py
│   │   └── test_agents.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend
│   ├── streamlit_app
│   │   ├── app.py
│   │   ├── pages
│   │   │   ├── dashboard.py
│   │   │   └── agent_control.py
│   │   ├── components
│   │   │   ├── agent_panel.py
│   │   │   └── logs_view.py
│   │   └── utils.py
│   ├── requirements.txt
│   └── Dockerfile
├── orchestrator-sdk
│   ├── python
│   │   ├── orchestrator.py
│   │   └── client.py
│   └── tests
│       └── test_client.py
├── infra
│   ├── docker-compose.yml
│   └── .env.example
├── scripts
│   ├── start_backend.sh
│   ├── start_frontend.sh
│   └── run_tests.sh
├── tests
│   └── e2e_test.py
├── pyproject.toml
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/narevignesh/multi-agent-orchestrator.git
   cd multi-agent-orchestrator
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install the required dependencies:
     ```
     pip install -r requirements.txt
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory.
   - Install the required dependencies:
     ```
     pip install -r requirements.txt
     ```

4. Configure environment variables:
   - Copy `.env.example` to `.env` in the `infra` directory and update the values as needed.

## Running the Application
- To start the backend server:
  ```
  ./scripts/start_backend.sh
  ```

- To start the frontend application:
  ```
  ./scripts/start_frontend.sh
  ```

## Testing
- To run the tests for the backend:
  ```
  cd backend
  pytest tests/
  ```

- To run the end-to-end tests:
  ```
  pytest tests/e2e_test.py
  ```

## Usage
- Access the Streamlit frontend at `http://localhost:8501`.
- Use the dashboard to monitor agent activities and control their operations.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.