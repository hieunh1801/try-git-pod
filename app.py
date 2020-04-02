from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Hello world")
    return "Hello Worrld"


@app.route("/login")
def login():
    print("Hello world")
    return "Login"

if __name__ == "__main__":
    app.run(port=5000, debug=True)