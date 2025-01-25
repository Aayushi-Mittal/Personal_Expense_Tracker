from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# To run: flask --app hello run
# https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application