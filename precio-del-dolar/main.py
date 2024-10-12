import json
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/minimum_price')
def minimum_price():
    with open('minimum_price.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)


if __name__ == '__main__':
    app.run()
