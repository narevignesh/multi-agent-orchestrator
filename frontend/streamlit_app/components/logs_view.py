from streamlit import st

def display_logs(logs):
    st.title("Agent Logs")
    if logs:
        for log in logs:
            st.write(log)
    else:
        st.write("No logs available.")

def fetch_logs():
    # Placeholder for fetching logs from the backend API
    # This function should call the backend API to retrieve logs
    return []

def main():
    logs = fetch_logs()
    display_logs(logs)

if __name__ == "__main__":
    main()