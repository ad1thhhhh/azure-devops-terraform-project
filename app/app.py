from flask import Flask
import os
import psutil
import socket
from datetime import datetime

app = Flask(__name__)

VERSION = os.getenv("VERSION", "dev")

@app.route("/")
def home():
    return {
        "message": "Repoxi DevOp-Monitor",
        "deployment_version": VERSION,
        "hostname": socket.gethostname(),
        "timestamp": datetime.utcnow().isoformat()
    }

@app.route("/cpu")
def cpu():
    return {
        "deployment_version": VERSION,
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "memory_usage_percent": psutil.virtual_memory().percent
    }

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
