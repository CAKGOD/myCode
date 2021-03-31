#!/usr/bin/env python
# coding=utf-8
import json as js

if __name__ == '__main__':
    data = js.load(open('../../data/country_city.json'))
    for i in data['data']:
        if i['name'] == '美国':
            print(i)
