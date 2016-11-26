[Identify Fraud From Enron Data](http://htmlpreview.github.io/?https://github.com/arjan-hada/Udacity-Data-Analyst/blob/master/P5-Identify-Enron-Fraud/final_project/P5-Identify-Fraud-From-Enron-Data.html)
==============================

## Project Overview
In 2000, Enron was one of the largest companies in the United States. By 2002, it had collapsed into bankruptcy due to widespread corporate fraud. In the resulting Federal investigation, a significant amount of typically confidential information entered into the public record, including tens of thousands of emails and detailed financial data for top executives. In this project, you will play detective, and put your new skills to use by building a person of interest identifier based on financial and email data made public as a result of the Enron scandal. To assist you in your detective work, we've combined this data with a hand-generated list of persons of interest in the fraud case, which means individuals who were indicted, reached a settlement or plea deal with the government, or testified in exchange for prosecution immunity.

**Starter code**      
on git: git clone https://github.com/udacity/ud120-projects.git      
Reads in the data, takes your features of choice, then puts them into a numpy array, which is the input form that most sklearn functions assume.

**Project requirements**      
Engineer the features, pick and tune an algorithm, and to test and evaluate your identifier. 

## Scripts and dataset
These files are inside final\_project folder

[**P5-Identify-Fraud-From-Enron-Data.html**](http://htmlpreview.github.io/?https://github.com/arjan-hada/Udacity-Data-Analyst/blob/master/P5-Identify-Enron-Fraud/final_project/P5-Identify-Fraud-From-Enron-Data.html) : Final report for evaluation

**P5-Identify-Fraud-From-Enron-Data.ipynb** : POI identifer script and report together in a notebook. When you open the notebook click the icon on top right to display dynamic visualizations.

**poi\_id.py** : My script for the POI identifier.

**final\_project\_dataset.pkl** : The dataset for the project, more details below. 

**tester.py** : Script for checking the results we get from poi\_id.py. Prints out the algorithm and evaluation metrics.

**tester\_with\_feature\_importances.py** : If using tree based classifiers this tester will print everything from tester.py plus feature importances of the features used.

**my_dataset.pkl, my\_classifier.pkl, my\_feature_list.pkl** : Three pickle files created when making my classifier. These can be tested using the tester.py script. 

## Features in the dataset

The features in the data fall into three major types, namely financial features, email features and POI labels.

**financial features**: ['salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees'] (all units are in US dollars)

**email features**: ['to_messages', 'email_address', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi'] (units are generally number of emails messages; notable exception is ‘email_address’, which is a text string)

**POI label**: [‘poi’] (boolean, represented as integer)




