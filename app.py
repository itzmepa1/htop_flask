from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route("/htop")
def htop():
    full_name = "Your Full Name"  # Replace with your actual name
    username = os.getlogin()
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    top_output = subprocess.getoutput("top -b -n 1 | head -n 10")

    return f"""
    <h2>System Stats</h2>
    <p><b>Name:</b> {full_name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
    <pre>{top_output}</pre>
    """
