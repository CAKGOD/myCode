#!/usr/bin/env python
# coding=utf-8
# @Date: 2021-01-13 10:00:00
# @Author: CAKGOD (17801030219@163.com)
# @Language : Python3

import math
import numpy as np

class nlp:
    def tf(self, word_list):
        word_fre_dict = {}
        for i in word_list:
            if i in word_fre_dict:
                word_fre_dict[i] =  word_fre_dict[i] + 1
            else:
                word_fre_dict[i] = 1
        tf_dict = {}
        for k, v in word_fre_dict.items():
            tf_dict[k] = v / len(word_list)
        return tf_dict

    
    def idf(self, word_list, article_list):
        word_ide_dict = {}
        for i in word_list:
            for j in article_list:
                if i in j:
                    if i in word_ide_dict:
                        word_ide_dict[i] = word_ide_dict[i] + 1
                    else:
                        word_ide_dict[i] = 1
        idf_dict = {}
        for k, v in word_ide_dict.items():
            idf_dict[k] = math.log(len(article_list) / v)
        return idf_dict


    def tfidf(self, tf_dict, idf_dict):
        tf_idf_dict = {}
        for k, v in tf_dict.items():
            tf_idf_dict[k] = tf_dict[k] * idf_dict[k]
        return tf_idf_dict


    def convert_word_list_to_graph(self, word_list, window_size):
        word_graph_dict = {}
        for i in set(word_list):
            word_graph_dict[i] = []
        for i in range(len(word_list)):
            left = (i - window_size) if (i - window_size) > 0 else 0
            right = (i + window_size) if (i + window_size) < len(word_list) else len(word_list)
            word_graph_dict[word_list[i]] = word_list[left: right]
        for k, v in word_graph_dict.items():
            word_neighbor_list = list(set(v))
            word_neighbor_list.remove(k)
            word_graph_dict[k] = word_neighbor_list
        return word_graph_dict

        
    def convert_word_graph_to_matrix(self, word_graph_dict):
        word_index_dict = {}
        word_list = word_graph_dict.keys()
        for i in enumerate(word_list):
            word_index_dict[i[1]] = i[0]
        word_word_array = np.zeros((len(word_list), len(word_list)))
        for k, v in word_graph_dict.items():
            for j in v:
                word_word_array[word_index_dict[k]][word_index_dict[j]] = 1
        for i in range(len(word_list)):
            word_word_array[:, i] /= sum(word_word_array[:, i])
        return word_word_array


    def text_rank(self, word_word_array, iteration_num, alpha):
        word_value_array = np.full((len(word_word_array), 1), 1 / len(word_word_array))
        for _ in range(iteration_num):
            word_value_array = 1 - alpha + alpha * np.dot(word_word_array, word_value_array)
        return word_value_array
        


if __name__ == '__main__':
    with open('../data/中文语料库/2014_corpus.txt') as f:
        data = [[j.split('/')[0] for j in i.strip().split(' ') if '/w' not in j] for i in f.readlines()]
    with open('../data/中文停用词/中文停用词.txt', encoding='utf-8') as f:
        stop_words = [i.strip() for i in f.readlines()]
    data_without_stopwords = [i for i in data if i not in stop_words]
    data_single = data_without_stopwords[0]
    nlp_tool = nlp()
    
    # tf idf
    #word_tfidf_dict = nlp_tool.tfidf(nlp_tool.tf(data_single), nlp_tool.idf(data_single, data_without_stopwords))
    #for i in sorted(word_tfidf_dict.items(), key=lambda s:s[1], reverse=True):
    #    print(i)
    
    # text rank
    word_graph_dict = nlp_tool.convert_word_list_to_graph(data_single, 5)
    word_word_array = nlp_tool.convert_word_graph_to_matrix(word_graph_dict)
    word_importance = nlp_tool.text_rank(word_word_array, 50, 0.8)
    
    new_list = []
    word_list = list(word_graph_dict.keys())
    for i in range(len(word_list)):
        new_list.append([word_list[i], word_importance[i][0]])
    print(sorted(new_list, key=lambda x: x[1], reverse=True))
    
