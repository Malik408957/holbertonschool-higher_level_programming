# task_01_jinja.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Jinja Template Task - Under Construction"

if __name__ == '__main__':
    app.run(debug=True)
