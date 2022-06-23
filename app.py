import pickle
from preprocessors.preproces import Preprocessor

def classificate(ulasan):
    tfidf = pickle.load(open('./vectorizers/tfidf.pkl', 'rb'))
    svm = pickle.load(open('./models/svc.pkl', 'rb'))
    pre = Preprocessor()
    ulasan = pre.filtering(ulasan)
    prediction = svm.predict(tfidf.transform([ulasan]))
    if prediction[0] == 0:
        return 'negative'
    return 'positive'

ulasan = input('Ulasan: ')
print('Sentiment: ', classificate(ulasan))