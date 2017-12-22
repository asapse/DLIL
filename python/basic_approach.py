import spacy
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

DATA_DIR = "../release1/trans-manu/"

dev_corpus = pd.read_csv(DATA_DIR + "dev.csv", sep='\t', header=None, names=['id', 'content', 'label'], quoting=3, keep_default_na=False)
train_corpus = pd.read_csv(DATA_DIR + "train.csv", sep='\t', header=None, names=['id', 'content', 'label'], quoting=3, keep_default_na=False)


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

scoring = ['precision_macro', 'recall_macro', 'precision_micro']

classifier = MultinomialNB()  # alpha = .01 ?
classifier.fit(X_train, y_train)

print(classifier.score(X_dev, y_dev))
