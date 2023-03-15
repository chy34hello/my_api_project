from flask import Flask, request, jsonify
import pandas as pd
import io

app = Flask(__name__)

@app.route('/process_csv', methods=['POST'])
def process_csv():
    csv_file = request.files.get('file')
    if not csv_file:
        return jsonify({'error': 'No file provided'}), 400

    try:
        df = pd.read_csv(io.StringIO(csv_file.read().decode('utf-8')))
        # Perform your desired operations on the dataframe here.
        # For this example, we'll just return the first 5 rows.
        result = df.head(5).to_dict(orient='records')
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
