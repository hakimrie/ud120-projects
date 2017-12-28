#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

numPeople = len(enron_data)
print numPeople
print len(enron_data["SKILLING JEFFREY K"])
numpoi = 0
hasQuantifiedSalary = 0
hasKnownEmailAddress = 0
hasNanTotalPayment = 0
isPoiAndHasNanTotalPayment = 0
for key, value in enron_data.items():
    if enron_data[key]['poi'] == 1:
        numpoi = numpoi + 1
        if (enron_data[key]['total_payments'] == 'NaN'):
            isPoiAndHasNanTotalPayment += 1
    if (enron_data[key]['salary'] != 'NaN'):
        hasQuantifiedSalary = hasQuantifiedSalary + 1
    if (enron_data[key]['email_address'] != 'NaN'):
        hasKnownEmailAddress += 1
    if (enron_data[key]['total_payments'] == 'NaN'):
        hasNanTotalPayment += 1

print "num POI ", numpoi
print "num hasQuantifiedSalary ", hasQuantifiedSalary
print "num hasKnownEmailAddress ", hasKnownEmailAddress
print "num hasNanTotalPayment %d or %f " % (hasNanTotalPayment, float(hasNanTotalPayment)/numPeople )
print "num isPoiAndHasNanTotalPayment %d or %f " % (isPoiAndHasNanTotalPayment, float(isPoiAndHasNanTotalPayment)/numPeople )

print enron_data["Prentice James".upper()]["total_stock_value"]
print "number of message of Wesley Colwell to POI: ", enron_data["Colwell Wesley".upper()]["from_this_person_to_poi"]
print "value stock options excersised to JK Skilling ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "total payment of J Skilling ", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "total payment of Kenneth Lay ", enron_data["LAY KENNETH L"]["total_payments"]
print "total payment Andrew Fastow ", enron_data["FASTOW ANDREW S"]["total_payments"]