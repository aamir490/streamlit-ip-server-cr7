
import streamlit as st
import requests
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import io
import requests

# -------------------------------------------------
# Host Info Viewer (Your new code)
st.title("Host Info Viewer")

# Function to get public IP
def get_public_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
        return ip
    except Exception as e:
        return f"Unable to get IP: {e}"

# Show public IP
public_ip = get_public_ip()
st.write(f"**Public IP Address:** {public_ip}")

# Show current time
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
st.write(f"**Current Time:** {current_time}")

# -------------------------------------------------
# Your original code below this line
st.title("Streamlit User Input and Image Upload Example")

# -------------------------------------------------
# User Input Section
st.header("User Authentication")
name = st.text_input('Enter your name:')
email = st.text_input('Enter your email:')
password = st.text_input('Enter password:', type='password')  # Secure text input
gender = st.selectbox('Select your gender', ['Male', 'Female', 'Others'])

# Button to trigger login
btn = st.button('Login')

# -------------------------------------------------
# Button Click Handling
if btn:
    # Simulate a loading process
    with st.spinner('Checking credentials...'):
        time.sleep(2)  # Simulate a delay for processing

    # Check credentials
    if email == 'cr7@gmail.com' and password == 'cr123':
        st.balloons()  # Show balloons on successful login
        st.success('Login Successful!')
        st.write(f'Welcome, {name}!')

        # Display current date
        today = datetime.date.today()
        st.write(f'Today\'s date is: {today}')

        # Display sample DataFrame
        df = pd.DataFrame({
            'Column 1': np.random.randn(5),
            'Column 2': np.random.randn(5)
        })
        st.write('Here is a sample DataFrame:')
        st.dataframe(df)

        # Display a simple plot
        st.write('Here is a sample plot:')
        fig, ax = plt.subplots()
        ax.plot(df['Column 1'], df['Column 2'], 'o-')
        st.pyplot(fig)

        # JSON Example
        json_data = {
            'user_name': name,
            'user': email,
            'status': 'Logged in',
            'gender': gender,
            'country': 'Portugal',
            'current_team': 'Al-Nassar'
        }
        st.write('### User Data in JSON format:')
        st.json(json_data)

    else:
        st.error('Login Failed! Please check your credentials.')

# -------------------------------------------------
# Image Upload Section
st.header("Image Upload Example")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # To read file as bytes:
    file_bytes = uploaded_file.read()
    st.image(file_bytes, caption='Uploaded Image', use_column_width=True)
    st.success('Image successfully uploaded!')
else:
    st.warning('No image uploaded yet.')

# -------------------------------------------------
# Subheader for CSV Data Upload
st.subheader('Upload your data:')

# Direct download link for the CSV file (update with your own URL)
csv_url = 'https://drive.google.com/uc?export=download&id=19RkLdzmXimOir4atgAdJv2LYMJVG7mKV'

# Function to read the CSV from the provided URL
@st.cache_data
def load_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.content.decode('utf-8')
        df = pd.read_csv(io.StringIO(data))
        return df
    except requests.RequestException as e:
        st.error(f"Error loading CSV file: {e}")
        return None

# Load data
df = load_data(csv_url)

# Check if data is loaded successfully
if df is not None:
    st.write('Here is the dataset:')
    st.dataframe(df)

    # Download CSV Option
    st.subheader('Download CSV:')
    download_option = st.radio("Would you like to download the dataset?", ('Yes', 'No'))

    if download_option == 'Yes':
        csv_data = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name='cr07.csv',
            mime='text/csv'
        )

    # Display a plot of the data
    st.subheader('Plot of the Data:')
    st.write('Choose columns to plot:')
    x_col = st.selectbox('X-axis:', df.columns)
    y_col = st.selectbox('Y-axis:', df.columns)

    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col], 'o-')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    st.pyplot(fig)

# -------------------------------------------------
# Progress Bar Example
st.header("Progress Bar Example")
progress_bar = st.progress(0)

# Simulate a long-running task
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.05)

st.write('Progress Complete!')
st.success('Profile Upload successfully!')
