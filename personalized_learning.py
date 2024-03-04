import os
import PyPDF2
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to extract text from PDF file
def extract_text_from_pdf(filepath):
    with open(filepath, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        extracted_text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()
    return extracted_text

# Route for displaying questions and answers
@app.route('/')
def display_questions():
    filepath = "C:/Users/Ratan/Desktop/try/notes1_personalisedLearninng.pdf"
    extracted_text = extract_text_from_pdf(filepath)

    # Split the text into chunks
    chunk_size = 4000
    chunks = [extracted_text[i:i + chunk_size] for i in range(0, len(extracted_text), chunk_size)]

    # Generate questions and answers for each chunk
    all_questions = []
    all_answers = []
    for chunk in chunks:
        prompt = f"This is a portion of the document content: {chunk}. Generate a relevant question and a concise answer."
        # Call your function for getting completion here (I'm assuming you have a function named get_completion)
        question = get_completion(prompt)
        all_questions.append(question)
        # Assuming you already have answers generated
        all_answers.append("Sample answer")  # Replace "Sample answer" with actual answers

    return render_template('questions.html', questions=all_questions, answers=all_answers)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change the port number to 5001
