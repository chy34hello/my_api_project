from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_csv_data():
    data = []
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
