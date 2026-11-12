from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Odessey Docker Web Server Assignment</h1>
    <p>Hello! My Docker container is running.</p>
    <p>Port Mapping: 8080 -> 5000</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)