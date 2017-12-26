#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################
# clf = svm.SVC(kernel='linear')
# rbf kernel
# clf = svm.SVC(C = 10.0, kernel='rbf')
# clf100 = svm.SVC(C = 100.0, kernel='rbf')
# clf1000 = svm.SVC(C = 1000.0, kernel='rbf')
clf10000 = svm.SVC(C = 10000.0, kernel='rbf')
# t0 = time()
# all data
#clf.fit(features_train, labels_train)
# 1% data
# clf.fit(features_train[:len(features_train)/100], labels_train[:len(labels_train)/100])
# print "training time c=10 :", round(time()-t0, 3), "s"
# t0 = time()
# clf100.fit(features_train[:len(features_train)/100], labels_train[:len(labels_train)/100])
# print "training time c=100 :", round(time()-t0, 3), "s"
# t0 = time()
# clf1000.fit(features_train[:len(features_train)/100], labels_train[:len(labels_train)/100])
# print "training time c=1000 :", round(time()-t0, 3), "s"
t0 = time()
clf10000.fit(features_train, labels_train)
print "training time c=10000:", round(time()-t0, 3), "s"

# print "prediction c=10"
# t0 = time()
# prediction = clf.predict(features_test)
# print "prediction time c=10:", round(time()-t0, 3), "s"
# accuracy = clf.score(features_test, labels_test)
# print "score c=10: %f " % accuracy

# print "prediction c=100"
# t0 = time()
# prediction = clf100.predict(features_test)
# print "prediction time c=10:", round(time()-t0, 3), "s"
# accuracy = clf100.score(features_test, labels_test)
# print "score c=100: %f " % accuracy

# print "prediction c=1000"
# t0 = time()
# prediction = clf1000.predict(features_test)
# print "prediction time c=1000:", round(time()-t0, 3), "s"
# accuracy = clf1000.score(features_test, labels_test)
# print "score c=1000: %f " % accuracy

print "prediction c=10000"
t0 = time()
prediction10 = clf10000.predict(features_test)
print "chris: ", sum(prediction10)
# print "prediction10 ", prediction10
# prediction26 = clf10000.predict([features_test[26]])
# print "prediction26 ", prediction26
# prediction50 = clf10000.predict([features_test[50]])
# print "prediction50 ", prediction50
print "prediction time c=10000:", round(time()-t0, 3), "s"
accuracy = clf10000.score(features_test, labels_test)
print "score c=10000: %f " % accuracy
