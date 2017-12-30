#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
for key, value in data_dict.items():
    print "key %s bonus %s" % (key, value["bonus"])
total = data_dict.pop("TOTAL", {})
data = featureFormat(data_dict, features)


### your code below
print type(data)
for point in data:
    salary = point[0]
    bonus = point[1]
    print "salary/bonus %s %s" % (salary, bonus)
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
