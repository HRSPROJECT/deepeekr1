import streamlit as st
import subprocess
import os
import time

st.title("Attempting to Run Ollama on Streamlit Cloud (Likely to Fail)")

st.header("Step 1: Attempting to install Ollama")

try:
    # Attempt to install Ollama
    st.write("Downloading Ollama...")
    ollama_install = subprocess.run(['curl', '-fsSL', 'https://ollama.com/install.sh', '-o', 'install.sh'], capture_output=True, text=True)

    if ollama_install.returncode == 0:
        st.write("Downloaded Ollama install script.")
    else:
        st.write(f"Error Downloading Ollama Install Script: {ollama_install.stderr}")

    st.write("Installing Ollama...")
    ollama_install = subprocess.run(['sh', 'install.sh'], capture_output=True, text=True)

    if ollama_install.returncode == 0:
        st.write("Installed Ollama.")
    else:
        st.write(f"Error Installing Ollama: {ollama_install.stderr}")
except Exception as e:
    st.write(f"Error during download and install: {e}")


st.header("Step 2: Attempting to pull the model")

try:
    # Attempt to pull the model
    st.write("Pulling deepseek-r1:1.5b model...")
    ollama_pull = subprocess.run(['ollama', 'pull', 'deepseek-r1:1.5b'], capture_output=True, text=True)
    if ollama_pull.returncode == 0:
        st.write("Pulled deepseek-r1:1.5b model.")
    else:
        st.write(f"Error Pulling the model: {ollama_pull.stderr}")
except Exception as e:
        st.write(f"Error pulling the model: {e}")

st.header("Step 3: Attempting to run the Ollama Server")
try:
    # Attempt to start the Ollama API Server
    st.write("Starting the Ollama Server...")
    ollama_serve = subprocess.Popen(['ollama', 'serve'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Keep printing server output, will likely fail
    time.sleep(5) # wait a short time to allow server to start (or fail)
    stdout, stderr = ollama_serve.communicate(timeout = 10) # wait 10 seconds to collect output
    if ollama_serve.returncode == None:
        st.write(f"Ollama server did not return a successful exit code. It may or may not be working correctly. Stderr: {stderr} ")
    elif ollama_serve.returncode == 0:
        st.write("Ollama server appears to have started correctly but this is unlikely in Streamlit Cloud.")
    else:
        st.write(f"Error Starting Ollama Server: {stderr}")

except Exception as e:
    st.write(f"Error starting Ollama server: {e}")
