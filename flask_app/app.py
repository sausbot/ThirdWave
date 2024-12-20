import jsonify

from flask import Flask, request, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def process():
    input_data = request.get_json()["data"]
    print(input_data)
    # Process the data
    result = some_processing_function(input_data)
    return {'result': result}

def some_processing_function(input_data):
    # Example processing function
    return f"Processed data: {input_data}"


if __name__ == "__main__":
    app.run("localhost", 6969)
