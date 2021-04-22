from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
from commons import *
import threading

app = Flask(__name__)
CORS(app)


@app.route("/cloudlamb/api/V1/health", methods=['GET'])
def health():
    response = "Alive"
    return response


@app.route("/cloudlamb/api/V1/save", methods=['POST'])  ## curl -d "id=1&nombre=manu" -X POST 'X.X.X.X/cloudlamb/api/V1/save'
def do_():
	if request.method == 'POST':
		data = request.form
		_id = data['id']
		nombre = data['nombre']
		response = put_dynamo(_id, nombre)
	return response


if __name__ == '__main__':
	app.run(host='0.0.0.0', port='8080')