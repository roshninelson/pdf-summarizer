from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    summary = ""

    if request.method == 'POST':

        pdf = request.files['pdf']

        reader = PyPDF2.PdfReader(pdf)

        text = ""

        for page in reader.pages:
            text += page.extract_text()

        summary = text[:1000]

    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)