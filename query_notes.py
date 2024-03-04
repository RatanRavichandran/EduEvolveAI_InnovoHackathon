from flask import Flask, render_template, request
import PyPDF2
import openai

# Replace with your actual OpenAI API key
openai.api_key = "API_KEY"

app = Flask(__name__)

# Function to extract text from PDF
def extract_text(filepath):
    with open(filepath, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        extracted_text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()
    return extracted_text

# Function to generate response using OpenAI API
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model, messages=messages, temperature=0
    )
    return response.choices[0].message["content"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_question = request.form["question"]
        if user_question.lower() == "exit":
            return render_template("index2.html", message="Exiting...")

        filepath = "C:/Users/Ratan/Desktop/innovo/notes1.pdf"  # Update with your file path
        context = extract_text(filepath)
        prompt = f"""
          User Question: {user_question}
          Context: {context}
        """

        response = get_completion(prompt)

        return render_template("index2.html", question=user_question, answer=response)
    else:
        return render_template("index2.html")

if __name__ == "__main__":
    app.run(port=8090)
    
