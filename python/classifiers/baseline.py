from classifier import Classifier
from sklearn.classifier import MultinomialNB

class Baseline(Classifier):
    """docstring for Baseline"""
    def __init__(self, MultinomialNB, feature_extractor):
        super(Baseline, self).__init__()
        self.arg = arg
