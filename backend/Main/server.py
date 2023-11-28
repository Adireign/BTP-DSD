from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from main import main
import os

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

@app.route('/pdf-files/<filename>', methods=['GET'])
def get_pdf(filename):
    pdf_directory = './'  # Update with the actual path to your PDF files
    return send_from_directory(pdf_directory, filename)

@app.route('/pdf-files', methods=['GET'])
def get_pdf_files():
    print("started it")
    pdf_files = [file for file in os.listdir('./') if file.endswith('.pdf')]
    return jsonify(pdf_files)


if __name__ == '__main__':
    app.run(debug=True)
