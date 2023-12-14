from flask import Flask, request, jsonify
from flask_cors import CORS
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


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


if __name__=="__main__":
    app.run(debug=True)