from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
import requests
import json

def get_sudoku(level=1):
    r = requests.get(f'http://www.cs.utep.edu/cheon/ws/sudoku/new/?level={level}&size=9')
    txt = r.text
    sudoku = json.loads(txt)["squares"]
    return sudoku

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

class Sudoku(Resource):
    def get(self):
        sudoku = get_sudoku()
        return sudoku

api.add_resource(Sudoku, "/")

if __name__=="__main__":
    app.run(port=5003, debug=True)

#http://127.0.0.1:5003/
