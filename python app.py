from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "i am almost a devops engineer"

if __name__ == "__main__":
    app.run(0.0.0.0)
