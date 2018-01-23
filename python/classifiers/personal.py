import pandas as pd
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from sklearn import metrics

import numpy as np
import itertools
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


class PersonalClf:
    def __init__(self, corpus_train, *, corpus_add=None):
        self.clf = SGDClassifier()
        stop_words = set(stopwords.words('french'))
        self.vectorizer = TfidfVectorizer(stop_words=stop_words, strip_accents='unicode', ngram_range=(1, 2))
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
        self.class_names = ['ETFC', 'ITNR', 'NVGO', 'TARF', 'PV', 'OBJT', 'VGC', 'HORR', 'RETT', 'CPAG', 'OFTP', 'JSTF',
                       'NULL', 'AAPL']

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

        y_pred = self.clf.predict(X_dev)

        print("Macro Precision:", metrics.precision_score(y_dev, y_pred, labels=self.class_names, average='macro'))
        print("Macro Recall:", metrics.recall_score(y_dev, y_pred, labels=self.class_names, average='macro'))
        print("Micro Pr/Re:", metrics.precision_score(y_dev, y_pred, labels=self.class_names, average='micro'))

        if full:
            print("==============")
            print(metrics.classification_report(y_dev, y_pred, labels=self.class_names))

        # self.show_confusion_matrix(y_dev, y_pred)

    def predict(self):
        pass

    @staticmethod
    def plot_confusion_matrix(cm, classes, title='Confusion matrix'):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        # print('Confusion matrix')
        # print(cm)

        plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)
        fmt = 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')

    def show_confusion_matrix(self, y_dev, y_pred):
        # Compute confusion matrix
        cnf_matrix = confusion_matrix(y_dev, y_pred, labels=self.class_names)
        np.set_printoptions(precision=2)

        # Plot confusion matrix
        plt.figure()
        self.plot_confusion_matrix(cnf_matrix, classes=self.class_names)
        plt.show()
