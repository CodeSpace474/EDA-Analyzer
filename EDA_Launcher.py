import subprocess
import webbrowser
import time
import sys
import socket
import os

# ================================
# CONFIG
# ================================
PORT = 8501
PYTHON_PATH = r"C:\Users\HP\AppData\Local\Programs\Python\Python311\python.exe"

# ================================
# CHECK IF PORT IS ACTIVE
# ================================
def is_port_open(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex(("localhost", port)) == 0

# ================================
# BASE DIRECTORY (EXE SAFE)
# ================================
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
    SCRIPT_PATH = os.path.join(os.path.dirname(BASE_DIR), "EDA_Analyzer.py")
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SCRIPT_PATH = os.path.join(BASE_DIR, "EDA_Analyzer.py")

# ================================
# LOCK FILE (PREVENT MULTI OPEN)
# ================================
LOCK_FILE = os.path.join(BASE_DIR, "app.lock")

if os.path.exists(LOCK_FILE):
    sys.exit()  # Exit if already running

# Create lock
open(LOCK_FILE, "w").close()

try:
    # ================================
    # START STREAMLIT SILENTLY
    # ================================
    process = subprocess.Popen(
        [
            PYTHON_PATH,
            "-m",
            "streamlit",
            "run",
            SCRIPT_PATH,
            f"--server.port={PORT}",
            "--server.headless=true",
            "--browser.gatherUsageStats=false",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # ================================
    # SMART WAIT FOR SERVER
    # ================================
    timeout = 15  # seconds
    start_time = time.time()

    while time.time() - start_time < timeout:
        if is_port_open(PORT):
            break
        time.sleep(0.5)

    # ================================
    # OPEN BROWSER
    # ================================
    time.sleep(1.5)  # small buffer for server readiness
    webbrowser.open(f"http://localhost:{PORT}")

    # ================================
    # KEEP APP RUNNING
    # ================================
    process.wait()

finally:
    # ================================
    # CLEANUP LOCK FILE
    # ================================
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)  # remove lock after exit
