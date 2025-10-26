from streamlit import st
import requests

API_URL = "http://localhost:8000/api/v1"  # Adjust the URL as needed

def fetch_agents():
    response = requests.get(f"{API_URL}/agents")
    return response.json() if response.status_code == 200 else []

def fetch_logs():
    response = requests.get(f"{API_URL}/logs")
    return response.json() if response.status_code == 200 else []

def main():
    st.title("Multi-Agent Orchestrator")
    
    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Dashboard", "Agent Control"])

    if page == "Dashboard":
        st.header("Dashboard")
        agents = fetch_agents()
        st.write("Current Agents:")
        st.json(agents)

        logs = fetch_logs()
        st.write("Logs:")
        st.json(logs)

    elif page == "Agent Control":
        st.header("Agent Control")
        agent_id = st.text_input("Enter Agent ID to control:")
        if st.button("Control Agent"):
            # Implement control logic here
            st.success(f"Controlling agent with ID: {agent_id}")

if __name__ == "__main__":
    main()