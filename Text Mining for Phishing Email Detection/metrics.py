# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 13:57:24 2017

@author: Pranav Yadav

Calculating Precision, Recall, F-Measure and Accuracy
"""

def precision(true_pos, false_pos):
    p = true_pos / (true_pos + false_pos)
    return p

def recall(true_pos, false_neg):
    r = true_pos / (true_pos + false_neg)
    return r

def f_measure(p, r):
    f1 = 2 * ((p*r)/(p+r))
    return f1

def acc_ham(true_pos, false_pos):
    acc = true_pos / (true_pos + false_pos)
    return acc

def acc_spam(true_neg, false_neg):
    acc = true_neg / (true_neg + false_neg)
    return acc

def acc(true_pos, false_pos, true_neg, false_neg):
    acc = (acc_ham(true_pos, false_pos) + acc_spam(true_neg, false_neg)) / 2
    return acc

#precision, recall, f1-measure and accuray for SVM
print("\nSVM")
print("Precision: ", precision(126, 4))
print("Recall: ", recall(126, 6))
print("F1-Measure: ", f_measure(precision(126, 4),recall(126, 6)))
print("Accuracy: ", acc(126, 4, 124, 6))

#precision, recall, f1-measure and accuray for Naive Bayes
print("\nNaive Bayes")
print("Precision: ", precision(129, 1))
print("Recall: ", recall(129, 9))
print("F1-Measure: ", f_measure(precision(129, 1),recall(129, 9)))
print("Accuracy: ", acc(129, 1, 121, 9))

#precision, recall, f1-measure and accuray for Random Forest
print("\nRandom Forest")
print("Precision: ", precision(124, 6))
print("Recall: ", recall(124, 4))
print("F1-Measure: ", f_measure(precision(124, 6),recall(124, 4)))
print("Accuracy: ", acc(124, 6, 126, 4))

#precision, recall, f1-measure and accuray for AdaBoost
print("\nAdaBoost")
print("Precision: ", precision(120, 10))
print("Recall: ", recall(120, 3))
print("F1-Measure: ", f_measure(precision(120, 10),recall(120, 3)))
print("Accuracy: ", acc(120, 10, 127, 3))

