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
print len(enron_data)
print 'features available ', len(enron_data["METTS MARK"])

# Finding total no of person of interest
poi_count = 0
for p in enron_data:
  if enron_data[p]["poi"] == True:
    poi_count += 1

print "POI count: ", poi_count

# What is the total value of the stock belonging to James Prentice?
print 'James Prentice stock value: ', enron_data["PRENTICE JAMES"]["total_stock_value"]

# How many email messages do we have from Wesley Colwell to persons of interest?
print 'Email from Wesley Colwell to POI: ', enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# What is the value of stock options exercised by Jeffrey K Skilling?
print 'Value of stock options by Jeffrey K Skilling: ', enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# Finding quantified salary and known email address
salary_count = 0
email_address = 0
for p in enron_data:
  if enron_data[p]["salary"] != 'NaN':
    salary_count += 1
  if enron_data[p]["email_address"] != 'NaN':
    email_address += 1

print "Quantified salary: ", salary_count
print "Known email address: ", email_address

# Finding number of people with no payments
no_total_payments = 0
for p in enron_data:
  if enron_data[p]["total_payments"] == 'NaN':
    no_total_payments += 1
print "People not having total payments: ", float(no_total_payments) / len(enron_data) * 100

# Counting POI with NaN
count_poi = 0
count_nan = 0
for k in enron_data:
  if enron_data[k]['poi'] == True:
    count_poi += 1
    if enron_data[k]['total_payments'] == "NaN":
      count_nan += 1
print "POI with NaN: ", float(count_nan)/count_poi * 100

# If you added in, say, 10 more data points which were all POIs,
# and put NaN for the total payments for those folks, the numbers you just calculated would change.
# What is the new number of people of the dataset? What is the new number of folks with NaN for total payments?
print 10 + len(enron_data)
new_total_payments = 10 + no_total_payments
print "After adding 10 NaN to Total payments: ", new_total_payments
