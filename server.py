"""
server.py implements the server interface layer between the android client and the Neural network
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello Neural Guide!"

if __name__ == "__main__":
    app.run()



