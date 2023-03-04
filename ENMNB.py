# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 01:12:31 2022

@author: adrie
"""

from sklearn.metrics import classification_report, f1_score, accuracy_score, precision_score, recall_score, multilabel_confusion_matrix
from sklearn.model_selection import train_test_split
 


import pandas as pd


from nltk.corpus import stopwords

from preprocessmethods import *


questions = pd.read_csv('faq3.csv', delimiter=",", encoding='cp1252')
X1 = questions.Intents
X2 = questions.Questions
X3 = questions.Responses
Y = questions.Intents



#function to remove punctuation

#store punctuation free text
X3= X3.apply(lambda x:remove_punctuation(x))
X2= X2.apply(lambda x:remove_punctuation(x))
X1= X1.apply(lambda x:remove_punctuation(x))

# #convert and store the questions and responses without punctuation to lower case
X3= X3.apply(lambda x: x.lower())
X2= X2.apply(lambda x: x.lower())
X1= X1.apply(lambda x: x.lower())



X1= X1.apply(lambda text: remove_stopwords(text))
X2= X2.apply(lambda text: remove_stopwords(text))
X3= X3.apply(lambda text: remove_stopwords(text))




X1= X1.apply(lambda text: lemmatize_words(text))
X2= X2.apply(lambda text: lemmatize_words(text))
X3= X3.apply(lambda text: lemmatize_words(text))

#remove URL

X1= X1.apply(lambda text: remove_urls(text))
X2= X2.apply(lambda text: remove_urls(text))
X3= X3.apply(lambda text: remove_urls(text))




X1= X1.apply(lambda text: special_char(text))
X2= X2.apply(lambda text: special_char(text))
X3= X3.apply(lambda text: special_char(text))



X_train, X_test, Y_train, Y_test = train_test_split(X2, Y, test_size= 0.2, random_state= 42)
# print(X_train.shape)
# print(X_test.shape)
# print(Y_train.shape)
# print(Y_test.shape)
   
from sklearn.feature_extraction.text import TfidfVectorizer

vect = TfidfVectorizer()
# vect.fit(X_train)

X_train_dtm = vect.fit_transform(X_train)


X_test_dtm = vect.transform(X_test)

from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()
# import timeit
# start = timeit.default_timer()
mnb.fit(X_train_dtm, Y_train)
# end = timeit.default_timer()
# print("Time taken for MNB model to be built: ", end - start)

Y_pred_label = mnb.predict(X_test_dtm)

# print(classification_report(Y_test, Y_pred_label, zero_division = 0))
# print(multilabel_confusion_matrix(Y_test, Y_pred_label))
# print("F1 Score is : ", f1_score(Y_test, Y_pred_label, average= 'macro'))
# print("Accuracy Score is : ", accuracy_score(Y_test, Y_pred_label))
# print("Precision is : ", precision_score(Y_test, Y_pred_label, average='micro'))
# print("Recall Score is : ", recall_score(Y_test, Y_pred_label, average='micro'))




# question = [input()]
# remove_punctuation(question[0])
# remove_stopwords(question[0])
# lemmatize_words(question[0])
# remove_urls(question[0])
# special_char(question[0])
# question[0].lower()
# question = vect.transform(question)

# category = mnb.predict(question[0])
# category = ",".join(str(x) for x in category)
# print(category)
   
# import csv

# dict_from_csv = {}

# with open('response3.csv', mode = 'r') as inp:
#     reader = csv.reader(inp)
#     dict_from_csv = {rows[0]: rows[1] for rows in reader}
# # print(dict_from_csv)    
# print(dict_from_csv[category])    
