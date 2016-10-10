#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL', 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

for name in data_dict:
  # float() does not include NaN values
  bonus = float(data_dict[name]["bonus"])
  salary = float(data_dict[name]["salary"])
  if bonus >= 5000000 and salary >= 1000000:
    print name, "bonus: ", data_dict[name]["bonus"], "salary: ", data_dict[name]["salary"]


### your code below
for point in data:
  salary = point[0]
  bonus = point[1]
  plt.scatter(salary, bonus)

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()
