from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "I am almost a Deveops Engineer!!"



app.run(host="0.0.0.0", port=5000)
