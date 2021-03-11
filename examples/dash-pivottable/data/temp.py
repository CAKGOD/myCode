#!/usr/bin/env python
# coding=utf-8

import os
import json as js

def get_all_files_name(path, file_list):
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        if os.path.isdir(file_path):
            get_all_files_name(file_path, file_list)
        else:
            file_list.append(file_path)

file_list = []
get_all_files_name('/home/cakgod/code/data/BCG/', file_list)

keyword_list = ['bank', 'pressure', 'nature']
data = [["orgnization", "time", "author", "title", "text",  "keywords", "count"]]
for i in file_list:
    if i.split('.')[-1] != 'json':
        continue
    tem_str = ''
    temp = js.load(open(i, 'r', encoding='utf-8'))
    temp_list = [temp['organization'], temp['time'], temp['author'], temp['title'], temp['artical']]
    for j in keyword_list:
        if j in temp_list[4]:
            temp_list.append(j)
            temp_list.append(temp_list[4].count(j))
            data.append(temp_list)

with open('./data.json', 'w') as f:
    js.dump(data, f)
