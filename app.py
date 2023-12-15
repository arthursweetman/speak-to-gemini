from flask import Flask, request, jsonify
from flask_cors import CORS
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import os


app = Flask(__name__)
CORS(app)

GOOGLE_API_KEY = "AIzaSyCYNqwGRNg2aFZEue0ZRl6NcOgfw0OR_Hc"
genai.configure(api_key=GOOGLE_API_KEY)


@app.route('/api/to-gemini', methods=['POST'])
def receive_data():
    data = request.get_data(as_text=True)  # Get the request body as a string
    # Process the received string
    print('Received string:', data)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(data)
    return jsonify({'result': response.text})


@app.route('/api/run-script')
def run_script():
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("How to tie a tie?")
    return {'result': response.text}


@app.route('/api/run-script2')
def run_script2():
    result = "Successful script 2 run!"
    return {'result': [result, "qwerty"]}


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))