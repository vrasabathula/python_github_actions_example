from flask import Flask
# This is used for sample testcase."""

app = Flask(__name__)


@app.route("/")
def index():
    """First app."""
    return "Welcomr to my first flask app"


if __name__ == "__main__":
    app.run()
