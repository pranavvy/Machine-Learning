# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:22:29 2017

@author: Pranav Yadav

Graphs of Confusion Martix
"""

import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 4
true_positive = (126, 129, 123, 120)
true_negative = (4, 1, 7, 10)
false_positive = (6, 9, 3, 3)
false_negative = (124, 121, 127, 127)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8
 
rects1 = plt.bar(index, true_positive, bar_width,
                 alpha=opacity,
                 color='b',
                 label='True Positive')
 
rects2 = plt.bar(index + bar_width, true_negative, bar_width,
                 alpha=opacity,
                 color='g',
                 label='True Negative')

rects3 = plt.bar(index + bar_width + bar_width, false_negative, bar_width,
                 alpha=opacity,
                 color='r',
                 label='False Negative')

rects4 = plt.bar(index + bar_width + bar_width + bar_width, false_positive, bar_width,
                 alpha=opacity,
                 color='y',
                 label='False Positive')

plt.xlabel('Algorithms')
plt.ylabel('Identified')
plt.title('Confusion Matrix')
plt.xticks(index + bar_width, ('SVM', 'Naive Bayes', 'RandomForest', 'AdaBoost'))
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
 
plt.tight_layout()
plt.show()