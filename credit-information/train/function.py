import pandas as pd
import numpy as np
from scipy.stats import ks_2samp
from sklearn.cross_validation import StratifiedKFold
#import xgboost as xgb
from sklearn.ensemble import GradientBoostingClassifier , RandomForestClassifier

class model():
    def __init__(self, df, clf = GradientBoostingClassifier()):
        self.clf = clf
        self.df = df
        useless_columns = ['label','user_id']
        feature = list(df.columns)
        for ul in useless_columns:
            if ul in feature:
                feature.remove(ul)
        self.feature = feature
    
    def KS(self, prediction, realvalue):
        return ks_2samp(prediction, realvalue)[0]

    def RunModel(self, train, label):
        self.clf.fit(train, label)
        return self.clf

    def k_fold_cv(self, n = 10):
        X = self.df[self.feature]
        y = self.df.label
        cv = StratifiedKFold(y, n_folds = n)
        self.ks = 0
        for train, test in cv:
            self.ks += self.KS(self.RunModel(X.ix[train,:], y[train]).predict_proba(X.ix[test,:])[:,1], y[test]) 
        self.ks /= float(n)
        return self.ks
    
    def show_ks(self):
        print 'The result is {0}'.format(self.ks)
    