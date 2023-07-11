import json
from flask import Flask, request, jsonify

app = Flask(__name__)



def index():
    return 'HHHHHHH'

@app.route('/')
def index():
    return 'HHHHHHH'


if __name__ == '__main__':
    app.run(debug=True)

