from streamlit import st

class AgentPanel:
    def __init__(self, agent_name, agent_status, agent_actions):
        self.agent_name = agent_name
        self.agent_status = agent_status
        self.agent_actions = agent_actions

    def display(self):
        st.subheader(f"Agent: {self.agent_name}")
        st.write(f"Status: {self.agent_status}")
        st.write("Available Actions:")
        for action in self.agent_actions:
            if st.button(action):
                self.perform_action(action)

    def perform_action(self, action):
        st.success(f"Performed action: {action} on agent: {self.agent_name}")