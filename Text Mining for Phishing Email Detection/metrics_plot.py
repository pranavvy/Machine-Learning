# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:28:38 2017

@author: Pranav Yadav

Metrics Graphs
"""

import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 4
precision = (0.97, 0.99, 0.95, 0.92)
recall = (0.95, 0.93, 0.97, 0.98)
f1_measure = (0.96, 0.96, 0.96, 0.95)
accuracy = (0.96, 0.96, 0.96, 0.95)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8
 
rects1 = plt.bar(index, precision, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Precision')
 
rects2 = plt.bar(index + bar_width, recall, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Recall')

rects3 = plt.bar(index + bar_width + bar_width, f1_measure, bar_width,
                 alpha=opacity,
                 color='r',
                 label='F1-Measure')

rects4 = plt.bar(index + bar_width + bar_width + bar_width, accuracy, bar_width,
                 alpha=opacity,
                 color='y',
                 label='Accuracy')

plt.xlabel('Algorithms')
plt.ylabel('Classification')
plt.title('Metrics')
plt.xticks(index + bar_width, ('SVM', 'Naive Bayes', 'RandomForest', 'AdaBoost'))
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
 
plt.tight_layout()
plt.show()