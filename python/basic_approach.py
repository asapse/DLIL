import spacy
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy as np
import itertools
from sklearn.model_selection import cross_validate

DATA_DIR = "../release1/trans-manu/"

dev_corpus = pd.read_csv(DATA_DIR + "dev.csv", sep='\t', header=None,
                         names=['id', 'content', 'label'], quoting=3, keep_default_na=False)
train_corpus = pd.read_csv(DATA_DIR + "train.csv", sep='\t', header=None,
                           names=['id', 'content', 'label'], quoting=3, keep_default_na=False)


train_content = list(train_corpus['content'])
train_label = list(train_corpus['label'])

dev_content = list(dev_corpus['content'])
dev_label = list(dev_corpus['label'])

print(len(train_content))
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_content)
X_dev = vectorizer.transform(dev_content)

y_train = train_label
y_dev = dev_label

scoring = ['f1_micro', 'f1_macro', 'precision_macro', 'recall_macro', 'precision_micro']

classifier = MultinomialNB()  # alpha = .01 ?

scores = cross_validate(classifier, X_train, y_train,
                        scoring=scoring, return_train_score=False, cv=10)
print('precision_macro : ' + str(scores['test_precision_macro'].mean()))
print('recall_macro : ' + str(scores['test_recall_macro'].mean()))
print('f1_macro : ' + str(scores['test_f1_macro'].mean()))
print('f1_micro : ' + str(scores['test_f1_micro'].mean()))
print()
#y_pred = classifier.fit(X_train, y_train).predict(X_dev)

#print(classifier.score(X_dev, y_dev))


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
"""
class_names = list(set(train_label))


# Compute confusion matrix
cnf_matrix = confusion_matrix(y_dev, y_pred, labels = class_names)
np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix, without normalization')


plt.show()
"""