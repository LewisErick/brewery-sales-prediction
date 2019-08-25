import csv
import json
from flask import Flask, jsonify
from flask_cors import CORS
from io import StringIO

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/v1.0/mensaje')
def create_task():
	io = StringIO()
	csvfile = open('input_data_train.csv', 'r')

	fieldnames = ('location', 'product','date','sa_quantity','temp_mean','temp_max','temp_min','sunshine_quant','event','price')
	reader = csv.DictReader( csvfile, fieldnames)
	i = 0
	next(reader)
	for row in reader:
		if i == 6:
			break
		json.dump(row, io)
		i = i + 1
	return jsonify(io.getvalue())

if __name__ == '__main__':
    app.run(debug=True)