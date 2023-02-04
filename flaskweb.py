from flask import Flask

app = Flask(__name__)

@app.route("http://54.173.252.10:5000/")
def hello():
    return "i am almost a devops engineer"

if __name__ == "__main__":
    app.run()

