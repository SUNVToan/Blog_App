from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

# load the environment variables
load_dotenv()

# create a Flask app
app = Flask(__name__)


# create a route decorator
@app.route("/")
def index():
    return render_template("index.html")


# create a route decorator: localhost:5000/user/toan
@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)


if __name__ == "__main__":
    app.run(debug=True)
