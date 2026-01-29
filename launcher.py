import webview
import subprocess
import time
import sys
import os

# Khởi động Streamlit trong background
streamlit_process = subprocess.Popen(
    ["streamlit", "run", "streamlit_app.py", "--server.headless=true"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Đợi một chút để Streamlit khởi động
print("Đang khởi động Streamlit...")
time.sleep(3)

# Tạo cửa sổ webview
webview.create_window("Trợ lý AI STEM", "http://localhost:8501", width=1200, height=800)
webview.start()

# Dọn dẹp khi đóng cửa sổ
streamlit_process.terminate()
streamlit_process.wait()
print("Đã đóng ứng dụng.")
