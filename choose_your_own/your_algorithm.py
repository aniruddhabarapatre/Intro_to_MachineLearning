#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score

classifier = {
  'adaboost': AdaBoostClassifier(n_estimators=100,learning_rate=1,algorithm="SAMME"),
  'kneigh': KNeighborsClassifier(n_neighbors=3),
  'randForest': RandomForestClassifier(n_estimators=15,criterion='entropy'),
  'svc': SVC(kernel="rbf", C=1),
  'naiveBayes': GaussianNB(),
  'dtree': DecisionTreeClassifier(min_samples_split=20)
}

for name, clf in classifier.iteritems():
  print name
  t0 = time()
  clf.fit(features_train, labels_train)
  print "\tTime to train: ", time() - t0, "s"

  pred = clf.predict(features_test)
  acc = accuracy_score(labels_test, pred)
  print "\tPrediction accuracy: ", acc

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
