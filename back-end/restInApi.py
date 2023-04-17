from flask import Flask, request, jsonify# request allows us to get data from front-end
from flask_cors import CORS

import sys

from demoScraper import findLocations

app = Flask(__name__)
CORS(app)

@app.route('/findlocations', methods=['GET'])
def rest_test():
    # GET allows front-end to get data from the back-end
    if request.method == 'GET':
        data = request.get_json()
        # calls function
        result = findLocations(data['loctype'], data['item'], data['address'], data['radius'])
        if result != None:
            # make into json file
            return jsonify(result)
        return {'Failed': 'idk'}

    return {
        'operation': 'not supported'
    }

