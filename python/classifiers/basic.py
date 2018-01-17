import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, f1_score, recall_score, precision_score
from sklearn.model_selection import cross_validate
from sklearn import metrics


class BasicClf:

    def __init__(self, corpus_train, *, corpus_add=None):
        self.clf = MultinomialNB(alpha=.1)
        self.vectorizer = CountVectorizer()
        if corpus_add is not None:
            x_train = pd.DataFrame(corpus_train)['content']
            x_add = pd.DataFrame(corpus_add)['content']
            self.X_train = self.extract_features(pd.concat([x_train, x_add]), fit=True)
            y_train = pd.DataFrame(corpus_train)['label']
            y_add = pd.DataFrame(corpus_add)['label']
            self.y_train = pd.concat([y_train, y_add])
        else:
            self.X_train = self.extract_features(pd.DataFrame(corpus_train)['content'], fit=True)
            self.y_train = pd.DataFrame(corpus_train)['label']
        self.train()

    def extract_features(self, X, fit=False):
        if fit is True:
            return self.vectorizer.fit_transform(X)
        else:
            return self.vectorizer.transform(X)

    def train(self):
        self.clf.fit(self.X_train, self.y_train)

    def evaluate(self, corpus_dev, *, full=False):
        X_dev = self.extract_features(pd.DataFrame(corpus_dev)['content'])
        y_dev = pd.DataFrame(corpus_dev)['label']

        class_names = list(set(y_dev))
        
        y_pred = self.clf.predict(X_dev)

        print("Macro Precision:", metrics.precision_score(y_dev, y_pred, labels=class_names, average='macro'))
        print("Macro Recall:", metrics.recall_score(y_dev, y_pred, labels=class_names, average='macro'))
        print("Micro Pr/Re:", metrics.precision_score(y_dev, y_pred, labels=class_names, average='micro'))

        if full:
            print("==============")
            print(metrics.classification_report(y_dev, y_pred))
        """
        f1_micro = f1_score(y_dev, y_pred, average='micro')
        f1_macro = f1_score(y_dev, y_pred, average='macro')
        recall_macro = recall_score(y_dev, y_pred, average='macro')
        precision_macro = precision_score(y_dev, y_pred, average='macro')
        precision_micro = precision_score(y_dev, y_pred, average='micro')

        return {'f1_macro': f1_macro, 'f1_micro': f1_micro, 'recall_macro': recall_macro, 'precision_macro': precision_macro, 'precision_micro': precision_micro}
        """
    def predict(self):
        pass
