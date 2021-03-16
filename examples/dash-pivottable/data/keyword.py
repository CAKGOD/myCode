#!/usr/bin/env python
# coding=utf-8
import json as js
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer

with open('./data.json') as f:
    data = js.loads(f.readline())

texts = [i[-3] for i in data]

tfidf_model = TfidfVectorizer()
tfidf_matrix = tfidf_model.fit_transform(texts)
word_dict = tfidf_model.get_feature_names()
print(word_dict)
print(tfidf_matrix)
