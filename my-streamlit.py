import streamlit as st
import requests
from datetime import datetime

# Function to get public IP
def get_public_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
        return ip
    except Exception as e:
        return f"Unable to get IP: {e}"

# Streamlit app
st.title("Host Info Viewer")

# Show public IP
public_ip = get_public_ip()
st.write(f"**Public IP Address:** {public_ip}")

# Show current time
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
st.write(f"**Current Time:** {current_time}")
