from streamlit import st

def display_dashboard():
    st.title("Multi-Agent Orchestrator Dashboard")
    
    st.header("Task Inputs")
    task_input = st.text_input("Enter your task:")
    
    if st.button("Submit Task"):
        # Here you would typically send the task to the backend for processing
        st.success(f"Task '{task_input}' submitted successfully!")

    st.header("Progress Logs")
    # This section would ideally fetch and display logs from the backend
    st.text_area("Logs", "No logs available yet...", height=300)

if __name__ == "__main__":
    display_dashboard()