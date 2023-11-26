from flask import Flask, request, jsonify
from flask_cors import CORS
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from main import main

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    print("started")
    data = request.json  # Get JSON payload from the request
    # Process the data as needed
    print('Received quiz data:', data)
    # print(data)
    print(data['tags'])
    print(data['numQuestions'])
    main(data['tags'],data['numQuestions'],data['level'])
    

    return jsonify({'message': 'Quiz submitted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
