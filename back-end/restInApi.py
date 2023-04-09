from flask import Flask, request, jsonify# request allows us to get data from front-end
from flask_cors import CORS

import sys

from demoScraper import demo

app = Flask(__name__)
CORS(app)

@app.route('/restdemo', methods=['GET', 'POST'])
def rest_test():
    # GET allows front-end to get data from the back-end
    if request.method == 'GET':
        # calls function
        result = demo()
        if result != None:
            # make into json file
            return jsonify(result)
        return {'Failed': 'idk'}
    
    # POST allows front-end to send datat to the back-end
    elif request.method == 'POST':
        data = request.get_json()
        # have to use stderr to print in flask
        print(data, file=sys.stderr)
        # make into json file
        return jsonify({
            'hello': 'world! (POST request)',
            'your item': data['item'],
            'your location': data['location']
        })

    return {
        'operation': 'not supported'
    }



