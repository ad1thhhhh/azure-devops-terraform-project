# Auto deployed test
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Networking CA01</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f6f9;
                    text-align: center;
                    padding-top: 100px;
                }
                .card {
                    background: white;
                    padding: 40px;
                    border-radius: 12px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                    display: inline-block;
                }
                h1 {
                    color: #2c3e50;
                }
                p {
                    color: #555;
                    font-size: 18px;
                }
                .footer {
                    margin-top: 20px;
                    font-size: 14px;
                    color: #888;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🚀 Networking Project is Live! - Version 2</h1>
                <p>Automated Continuous Deployment is working successfully.</p>
                <div class="footer">
                    Built using Python-Flask
                </div>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
