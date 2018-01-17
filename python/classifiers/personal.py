import pandas as pd
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from sklearn import metrics


class PersonalClf:
    def __init__(self, corpus_train):
        self.clf = SGDClassifier()
        stop_words = set(stopwords.words('french'))
        self.vectorizer = TfidfVectorizer(stop_words=stop_words, strip_accents='unicode', ngram_range=(1, 2))
        self.y_train = pd.DataFrame(corpus_train)['label']
        self.X_train = self.extract_features(pd.DataFrame(corpus_train)['content'], fit=True)
        self.train()

    def extract_features(self, X, fit=False):
        if fit is True:
            return self.vectorizer.fit_transform(X)
        else:
            return self.vectorizer.transform(X)

    def train(self):
        self.clf.fit(self.X_train, self.y_train)

    def evaluate(self, corpus_dev):
        X_dev = self.extract_features(pd.DataFrame(corpus_dev)['content'])
        y_dev = pd.DataFrame(corpus_dev)['label']

        class_names = list(set(y_dev))

        y_pred = self.clf.predict(X_dev)

        print("Macro Precision:", metrics.precision_score(y_dev, y_pred, labels=class_names, average='macro'))
        print("Macro Recall:", metrics.recall_score(y_dev, y_pred, labels=class_names, average='macro'))
        print("Micro Pr/Re:", metrics.precision_score(y_dev, y_pred, labels=class_names, average='micro'))

        print("==============")
        print(metrics.classification_report(y_dev, y_pred, labels=class_names))

    def predict(self):
        pass
