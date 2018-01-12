import spacy
import pandas as pd

from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy as np
import itertools
from sklearn.model_selection import cross_validate

import warnings
from sklearn import metrics
from sklearn.feature_selection import SelectKBest, chi2


def warn(*args, **kwargs):
    pass
warnings.warn = warn


def plot_confusion_matrix(cm, classes, title='Confusion matrix'):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    print('Confusion matrix')
    print(cm)

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


DATA_DIR = "../release1/trans-manu/"

dev_corpus = pd.read_csv(DATA_DIR + "dev.csv", sep='\t', header=None,
                         names=['id', 'content', 'label'], quoting=3, keep_default_na=False)
train_corpus = pd.read_csv(DATA_DIR + "train.csv", sep='\t', header=None,
                           names=['id', 'content', 'label'], quoting=3, keep_default_na=False)


train_content = list(train_corpus['content'])
train_label = list(train_corpus['label'])

dev_content = list(dev_corpus['content'])
dev_label = list(dev_corpus['label'])

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_content)
X_dev = vectorizer.transform(dev_content)

y_train = train_label
y_dev = dev_label
"""
ch2 = SelectKBest(chi2)
X_train = ch2.fit_transform(X_train, y_train)
X_dev = ch2.transform(X_dev)
"""
class_names = list(set(train_label))

scoring = ['f1_micro', 'f1_macro', 'precision_macro', 'recall_macro', 'precision_micro']

# classifier = MultinomialNB(alpha=.01)  # alpha = .01 ?
classifier = svm.LinearSVC(C=0.01, penalty="l1", dual=False)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_dev)

# print(classifier.score(X_dev, y_dev))
print("Recall UA:", metrics.recall_score(y_dev, y_pred, labels=class_names, average='macro'))
print("Recall WA:", metrics.recall_score(y_dev, y_pred, labels=class_names, average='weighted'))
print("Precision UA:", metrics.precision_score(y_dev, y_pred, labels=class_names, average='macro'))
print("Precision WA:", metrics.precision_score(y_dev, y_pred, labels=class_names, average='weighted'))

print("==============")
clf_metrics = metrics.precision_recall_fscore_support(y_dev, y_pred, labels=class_names)
print("Precision: ", clf_metrics[0])
print("Recall: ", clf_metrics[1])
print("F-score: ", clf_metrics[2])
print("Support:", clf_metrics[3])
print(class_names)

# Compute confusion matrix
cnf_matrix = confusion_matrix(y_dev, y_pred, labels=class_names)
np.set_printoptions(precision=2)

# Plot confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix')
plt.show()
