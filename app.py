from flask import Flask

# initializing a variable of Flask
app = Flask(__name__)


# decorating index function with the app.route
@app.route('/')
def index():
    return "Welcome, This is the home page"


if __name__ == "__main__":
    app.run()

