from flask import Flask, request, jsonify, send_from_directory, send_file
from flask_cors import CORS
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from main import main
import os
import io
from generateAssessment import generateAssessment

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    data = request.json  # Get JSON payload from the request
    # Process the data as needed
    print('Received quiz data for PDF generation:', data)

    ans = main(data['tags'],data['numQuestions'],data['level'])

    return jsonify({'message': 'Quiz submitted successfully'})

@app.route('/startAssessment', methods=['POST'])
def startAssessment():
    data = request.json
    print('Received quiz data to generate assessment:', data)

    questionDetails = generateAssessment(data['tags'],data['numQuestions'],data['level'])
    print(questionDetails)

    return jsonify({'questions': questionDetails})
    
@app.route('/submit_assessment', methods=['POST'])
def submit_assessment():
    data = request.json
    print('Recieved assessment data')
    print(data)
    return jsonify({'work-done': 'done work'})


@app.route('/pdf-files/<filename>', methods=['GET'])
def get_pdf(filename):
    pdf_directory = './PDF/'  # Update with the actual path to your PDF files
    return send_from_directory(pdf_directory, filename)

@app.route('/pdf-files', methods=['GET'])
def get_pdf_files():
    print("started it")
    pdf_files = [file for file in os.listdir('./PDF') if file.endswith('.pdf')]
    return jsonify(pdf_files)




if __name__ == '__main__':
    app.run(debug=True)
