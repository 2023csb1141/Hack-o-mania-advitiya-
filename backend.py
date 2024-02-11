from flask import Flask, request, jsonify
import string
from nltk.corpus import stopwords
# import pandas as pd
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from joblib import load,dump

def process_text(text):
    no_punc = [char for char in text if char not in string.punctuation]
    no_punc = ''.join(no_punc)
    
    stopw= set(stopwords.words('english'))
    return ' '.join([word for word in no_punc.split() if word.lower() not in stopw ])

def stemming (text):
    stemmer = PorterStemmer()
    return ''.join([stemmer.stem(word) for word in text])

# text = "Hey there! This is a sample review, which happkendens to contain punctuations."

# print(text)



backend = Flask(__name__)

@backend.route('/')
def index():
    return backend.send_static_file('Web_page_main.htm')

@backend.route('/predict', methods=['POST'])
def predict():
    data = request.json
    subject = data['subject']
    body = data['body']
    text= body + " " + subject
    text= process_text(text)
    text= stemming(text)
    count_vectorizer = CountVectorizer()
    text_vectorized = count_vectorizer.transform(text.split())

    
    # Implement your ML model or processing logic here
    # For example, let's just return a sample response
    model= load('mail_phishing_detection_model.joblib')
    result = model.predict(text_vectorized)
    result = 'phishing' if result == 1 else 'not phishing'
    
    return jsonify({'result': result})

if __name__ == '__main__':
    backend.run(debug=True)
