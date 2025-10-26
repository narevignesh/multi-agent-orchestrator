from streamlit import st
import requests

# Set the API endpoint for the backend
API_URL = "http://localhost:8000/api/v1"

def get_agents():
    response = requests.get(f"{API_URL}/agents")
    return response.json() if response.status_code == 200 else []

def control_agent(agent_id, action):
    response = requests.post(f"{API_URL}/agents/{agent_id}/control", json={"action": action})
    return response.json() if response.status_code == 200 else {}

st.title("Agent Control Panel")

agents = get_agents()

if agents:
    selected_agent = st.selectbox("Select an Agent", [agent['name'] for agent in agents])
    agent_id = next(agent['id'] for agent in agents if agent['name'] == selected_agent)

    action = st.radio("Select Action", ["Start", "Stop", "Restart"])

    if st.button("Execute"):
        result = control_agent(agent_id, action.lower())
        st.success(f"Action '{action}' executed on agent '{selected_agent}': {result}")
else:
    st.warning("No agents available.")