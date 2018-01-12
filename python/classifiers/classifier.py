from sklearn.metrics import get_scorer, f1_score, precision_score, recall_score


class Classifier:

    def __init__(self, clf, clf_param, feature_extractor):
        self.classifier = clf.__init__(clf_param)
        self.feature_extractor = feature_extractor
        self.X_train = None
        self.X_dev = None
        self.X_test = None
        self.y_train = None
        self.y_dev = None
        self.y_test = None

    def extract_features(self, train_corpus):
        self.X_train = self.feature_extractor(train_corpus, fit=True)

    def train(self, y_train):
        self.y_train = y_train
        clf.fit(self.X_train, self.y_train)

    def evaluate(self, y_dev):
        self.y_dev = y_dev
        self.X_dev = feature_extractor(dev_corpus, fit=False)
        y_pred = clf.predict(self.X_dev)

        f1_micro = f1_score(self.y_dev, y_pred, average='micro')
        f1_macro = f1_score(self.y_dev, y_pred, average='macro')
        recall_macro = recall_score(self.y_dev, y_pred, average='macro')
        precision_macro = precision_score(self.y_dev, y_pred, average='macro')
        precision_micro = precision_score(self.y_dev, y_pred, average='micro')

        return {'f1_macro': f1_macro, 'f1_micro': f1_micro, 'recall_macro': recall_macro, 'precision_macro': precision_macro, 'precision_micro': precision_micro}

    def test(self):
        return clf.predict()
