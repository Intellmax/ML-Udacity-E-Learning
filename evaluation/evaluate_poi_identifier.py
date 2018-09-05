#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_unix_dataset.pkl", "rb"))

### add more features to features_list!
features_list = ["poi", 'salary']

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### your code goes here 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)
print(len(X_test))
X_train = X_train[:30]
y_train = y_train[:30]
print("Length of X_train {}".format(len(X_train)))

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
pred = clf.predict(X_test)

score = accuracy_score(y_test, pred)
print("ACCURACY IS ", score)

matrix = confusion_matrix(y_test, pred)
print(matrix)

precision = precision_score(y_test, pred, average='micro')
print('Precision is {}'.format(precision))

recall = recall_score(y_test, pred, average='micro')
print("Recall is {}".format(recall))

#just test
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
matrix = confusion_matrix(true_labels, predictions)
print(matrix)
f1 = f1_score(true_labels, predictions)
print (f1)