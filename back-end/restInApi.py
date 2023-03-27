from flask import Flask
from flask import request

from demoScraper import demo

app = Flask(__name__)

@app.route('/restdemo', methods=['GET', 'POST'])
def grocery_test():
    if request.method == 'GET':
        result = demo()
        if result != None:
            return result
        return {'idk': 'idk'}
    elif request.method == 'POST':
        return {
            'hello': 'world! (POST request)'
        }

    return {
        'operation': 'not supported'
    }



