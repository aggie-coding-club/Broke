from flask import Flask, request, jsonify# request allows us to get data from front-end
from flask_cors import CORS

from demoScraper import findLocations

app = Flask(__name__)
CORS(app)

@app.route('/findlocations', methods=['POST'])
def rest_test():
    # POST request to handle the data request from the front-end
    if request.method == 'POST':
        data = request.get_json()
        # Calls the back-end scaper
        result = findLocations(data['loctype'], data['item'], data['address'], data['radius'])
        if result != None:
            # make into json object and return
            return jsonify(result)
        return {'Failed': 'idk'}

    return {
        'operation': 'not supported'
    }

