from flask import Flask, request, jsonify
from flask_cors import CORS

import sys

from demoScraper import demo

app = Flask(__name__)
CORS(app)

@app.route('/restdemo', methods=['GET', 'POST'])
def grocery_test():
    if request.method == 'GET':
        result = demo()
        if result != None:
            return jsonify(result)
        return {'Failed': 'idk'}
    elif request.method == 'POST':
        data = request.get_json()
        print(data, file=sys.stderr)
        return jsonify({
            'hello': 'world! (POST request)',
            'your item': data['item'],
            'your location': data['location']
        })

    return {
        'operation': 'not supported'
    }



