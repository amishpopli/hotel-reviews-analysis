from flask import Flask, render_template, request, url_for
from helperFunctions import *
import pickle


loaded_bow_model = None
loaded_tfidf_model = None
vectorizer_bow = None
vectorizer_tfidf = None
app = Flask(__name__)


# load bow model
def loaded_bow_model():
    global loaded_bow_model
    with open('../models/model_bow.pkl', 'rb') as file:
        loaded_bow_model = pickle.load(file)


# load transformer bow model
def vectorizer_bow():
    global vectorizer_bow
    with open('../models/transformer_bow.pkl', 'rb') as file:
        vectorizer_bow = pickle.load(file)


# load tfidf model
def loaded_tfidf_model():
    global loaded_tfidf_model
    with open('../models/model_tfidf.pkl', 'rb') as file:
        loaded_tfidf_model = pickle.load(file)


# load transformer tfidf model
def vectorizer_tfidf():
    global vectorizer_tfidf
    with open('../models/transformer_tfidf.pkl', 'rb') as file:
        vectorizer_tfidf = pickle.load(file)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = [_ for _ in request.form.values()]
        train_data = [text_process(data[0] + ' ' + data[1])]
        model = data[2]
        if model == 'bow':
            train_data = vectorizer_bow.transform(train_data)
            prediction = loaded_bow_model.predict(train_data)[0]
        else:
            train_data = vectorizer_tfidf.transform(train_data)
            prediction = loaded_tfidf_model.predict(train_data)[0]

        save_prediction(data, prediction)
        return render_template("index.html", prediction_text=f'The predicted rating of the review is: '
                                                             f'{np.round(prediction,2)}')


if __name__ == '__main__':
    loaded_bow_model()
    vectorizer_bow()
    loaded_tfidf_model()
    vectorizer_tfidf()
    app.run(debug=True)
