import pandas as pd
import numpy as np
import itertools
import warnings
import matplotlib.pyplot as plt

from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.ensemble import VotingClassifier

from spacy.lang.fr.stop_words import STOP_WORDS
from spacy.lang.fr import French
import spacy
import os

from nltk.corpus import stopwords


def warn(*args, **kwargs):
    pass
warnings.warn = warn


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


DATA_DIR = "../../release1/trans-manu/"
# DATA_DIR = "../../release2/"

dev_corpus = pd.read_csv(DATA_DIR + "dev.csv", sep='\t', header=None,
                         names=['id', 'content', 'label'], quoting=3, keep_default_na=False)
train_corpus = pd.read_csv(DATA_DIR + "train.csv", sep='\t', header=None,
                           names=['id', 'content', 'label'], quoting=3, keep_default_na=False)


train_content = list(train_corpus['content'])
train_label = list(train_corpus['label'])

dev_content = list(dev_corpus['content'])
dev_label = list(dev_corpus['label'])

stop_words = set(stopwords.words('french'))
vectorizer = TfidfVectorizer(stop_words=stop_words, strip_accents='unicode', ngram_range=(1, 3))

X_train = vectorizer.fit_transform(train_content)
X_dev = vectorizer.transform(dev_content)

y_train = train_label
y_dev = dev_label

class_names = list(set(train_label))

clf1 = MultinomialNB(alpha=0.1)
clf2 = svm.LinearSVC(C=1.5, penalty="l1", dual=False)
clf3 = SGDClassifier()

classifier = VotingClassifier(estimators=[('mnb', clf1), ('lsvc', clf2), ('lr', clf3)])

classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_dev)

print("Recall UA:", metrics.recall_score(y_dev, y_pred, labels=class_names, average='macro'))
print("Recall WA:", metrics.recall_score(y_dev, y_pred, labels=class_names, average='weighted'))
print("Precision UA:", metrics.precision_score(y_dev, y_pred, labels=class_names, average='macro'))
print("Precision WA:", metrics.precision_score(y_dev, y_pred, labels=class_names, average='weighted'))

print("==============")
print(metrics.classification_report(y_dev, y_pred, target_names=class_names))

# Compute confusion matrix
cnf_matrix = confusion_matrix(y_dev, y_pred, labels=class_names)
np.set_printoptions(precision=2)

# Plot confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix')
plt.show()