from flask import Flask, render_template, request
import re

app = Flask(__name__)

def count_tokens(paragraph):
    # Split the paragraph into tokens using regex to account for spaces and punctuation
    tokens = re.findall(r'\b\w+\b', paragraph)
    return tokens

@app.route('/', methods=['GET', 'POST'])
def index():
    word_count = 0
    sentence_count = 0
    token_count = 0
    tokens = []

    if request.method == 'POST':
        paragraph = request.form['paragraph']
        tokens = count_tokens(paragraph)
        word_count = len(tokens)
        sentence_count = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')
        token_count = len(tokens)

    return render_template('index.html', word_count=word_count, sentence_count=sentence_count, token_count=token_count, tokens=tokens)

if __name__ == '__main__':
    app.run(debug=True)