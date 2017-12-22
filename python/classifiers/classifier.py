

class Classifier():
    def __init__(self, clf, feature_extractor):
        self.classifier = clf.__init__()
        self.feature_extractor = feature_extractor
        self.X_train = None
        self.X_dev = None
        self.X_test = None
        self.y_train = None
        self.y_dev = None
        self.y_test = None

    def extract_features(corpus):
        pass

    def train(self):
        clf.fit()
