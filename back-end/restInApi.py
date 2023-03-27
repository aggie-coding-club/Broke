from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/grocerytest', methods=['GET', 'POST'])
def grocery_test():
    if request.method == 'GET':
        return {
            'hello': 'world! (GET request)'
        }
    elif request.method == 'POST':
        return {
            'hello': 'world! (POST request)'
        }

    return {
        'operation': 'not supported'
    }



