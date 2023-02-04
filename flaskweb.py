from flask import Flask

app = Flask(__name__)


@app.route('54.173.252.10/')
def hello():
    return 'I am almost a Devops Engineer'
  
