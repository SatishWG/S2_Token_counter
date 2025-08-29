# Token Counter App

This is a simple single-page application built with Flask that allows users to input a paragraph and receive counts for words, sentences, and tokens. The application splits the input based on spaces and punctuation marks to provide accurate counts.

## Project Structure

```
token-counter
├── static
│   └── style.css
├── templates
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
```

## Instructions to Run the App

1. **Install Dependencies**: Open your terminal and navigate to the project directory. Run the following command to install the required packages using UV:

   ```
   uv install -r requirements.txt
   ```

2. **Run the Application**: After the dependencies are installed, you can run the Flask application with the following command:

   ```
   uv run app.py
   ```

3. **Access the App**: Open your web browser and go to `http://127.0.0.1:5000` to access the token counter app. You can enter a paragraph in the provided form and submit it to see the word, sentence, and token counts.