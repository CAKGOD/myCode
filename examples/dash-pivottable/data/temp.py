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

keyword_list = ['china', 'huawei', 'weapon', 'war', 'AI', 'machine learning', 'deep learning', 'protein folding', 'meteorological', 'COVID-19', '5G', 'army']
data = [["orgnization", "time", "keywords", "count"]]
for i in file_list:
    if i.split('.')[-1] != 'json':
        continue
    temp = js.load(open(i, 'r', encoding='utf-8'))
    if temp['time'] == '':
        new_time = 'unknown'
    else:
        new_time = temp['time']
    for j in keyword_list:
        if j in temp['artical']:
            temp_list = [temp['organization'], new_time]
            temp_list.append(j)
            temp_list.append(temp['artical'].count(j))
            data.append(temp_list)

with open('./data.json', 'w') as f:
    js.dump(data, f)
