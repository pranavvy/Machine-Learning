# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:17:56 2017

@author: Pranav Yadav

Text Mining for Phishing Email Detection
"""

import os
import numpy as np
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import confusion_matrix

#generating a dictionary
def make_Dictionary(train_dir):
    emails = [os.path.join(train_dir,f) for f in os.listdir(train_dir)]    
    all_words = []       
    for mail in emails:    
        with open(mail) as m:
            for i,line in enumerate(m):
                if i == 2: #body of email starts at the 3rd line
                    words = line.split()
                    all_words += words
    
    dictionary = Counter(all_words)
#non-word removal
    list_to_remove = list(dictionary)
    for item in list_to_remove:
        if item.isalpha() == False: 
            del dictionary[item]
        elif len(item) == 1:
            del dictionary[item]
    dictionary = dictionary.most_common(3000)
    return dictionary

#generates a feature vector matrix
#rows(i) denote files in train set & columns(j) denote words in the dictionary
#value at index 'ij' repersents the occurance of jth word in ith file
def extract_features(mail_dir): 
    files = [os.path.join(mail_dir,fi) for fi in os.listdir(mail_dir)]
    features_matrix = np.zeros((len(files),3000))
    docID = 0;
    for fil in files:
      with open(fil) as fi:
        for i,line in enumerate(fi):
          if i == 2:
            words = line.split()
            for word in words:
              wordID = 0
              for i,d in enumerate(dictionary):
                if d[0] == word:
                  wordID = i
                  features_matrix[docID,wordID] = words.count(word)
        docID = docID + 1     
    return features_matrix
    
#dictionary of words with its frequency
train_dir = 'C:\\Users\\100557540\\Google Drive\\Pranav\\IITROPAR\\Dr. Puneet Goyal\\Main papers to implement\\text mining for phising email detetcion\\train-mails'
dictionary = make_Dictionary(train_dir)

#feature vectors for training emails & its labels
train_labels = np.zeros(702)
train_labels[351:701] = 1
train_matrix = extract_features(train_dir)

#training SVM and Naive Bayes classifiers
model1 = LinearSVC()
model2 = MultinomialNB()
model3 = RandomForestClassifier()
model4 = AdaBoostClassifier()

model1.fit(train_matrix,train_labels)
model2.fit(train_matrix,train_labels)
model3.fit(train_matrix, train_labels)
model4.fit(train_matrix, train_labels)

#test unseen mail for spam
test_dir = 'C:\\Users\\100557540\\Google Drive\\Pranav\\IITROPAR\\Dr. Puneet Goyal\\Main papers to implement\\text mining for phising email detetcion\\test-mails'
test_matrix = extract_features(test_dir)
test_labels = np.zeros(260)
test_labels[130:260] = 1

result1 = model1.predict(test_matrix)
result2 = model2.predict(test_matrix)
result3 = model3.predict(test_matrix)
result4 = model4.predict(test_matrix)

#confusion matrix for SVM and Naive Bayes models
print(confusion_matrix(test_labels,result1))
print(confusion_matrix(test_labels,result2))
#confusion matrix for RandomForest and AdaBoost models
print(confusion_matrix(test_labels,result3))
print(confusion_matrix(test_labels,result4))


