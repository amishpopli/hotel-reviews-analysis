import os
import pandas as pd
from csv import writer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import numpy as np


def text_process(text):
    if type(text) == float:
        return ""
    else:
        nopunc = [i.lower() for i in text if (i not in string.punctuation) & (i.isdigit() is False)]
        nopunc_text = ''.join(nopunc)
        lemmatizer = WordNetLemmatizer()
        nonpunc_nonstopwords_lemma_text = [lemmatizer.lemmatize(i) for i in nopunc_text.split()
                                           if i not in stopwords.words('english')]
        text = " ".join(nonpunc_nonstopwords_lemma_text)
        return text


# save predictions
def save_prediction(data, prediction):
    row = np.array(data + [prediction])
    dataframe = pd.DataFrame(row.reshape(-1, len(row)),
                             columns=['review_text', 'review_title', 'model', 'reviews_ratings'])
    if os.path.isfile('../storage/all_predictions.csv'):
        with open('../storage/all_predictions.csv', 'a') as file:
            writer_object = writer(file)
            writer_object.writerow(row)
    else:
        dataframe.to_csv('../storage/all_predictions.csv', index=False)


