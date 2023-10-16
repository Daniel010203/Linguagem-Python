from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Leia a documentação e explore o site do Flask : https://flask.palletsprojects.com/en/3.0.x/