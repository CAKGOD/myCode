import os
import json


def get_file_name(data_path):
    for root, dirs, files in os.walk(data_path):
        return files


def to_csv(path):
    f_a = open('zulip.txt', 'a')

    file_name_list = get_file_name(path)
    for file_name in file_name_list:
        
        with open(path + file_name) as f:
            data = f.readlines()
        
        for i in data:
            temp = ''
            if i[0:6] == '发送者姓名：':
                temp += i.strip()[6:]
                temp += '\t'
            elif i[0:6] == '发送者邮箱：':
                temp += i.strip()[6:]
                temp += '\t'
            elif i[0:3] == '时间：':
                temp += i.strip()[3:]
                temp += '\t'
            elif i[0:3] == '主题：':
                temp += i.strip()[3:]
                temp += '\t'
            elif i[0:3] == '内容：':
                temp += i.strip()[3:]
                temp += '\n'
            else:
                continue
            f_a.write(temp)


def to_dict(path):
    zulip_record_id = 0
    f_w = open('zulip_dict.json', 'w')

    dict_list = []

    file_name_list = get_file_name(path)
    for file_name in file_name_list:
       
        with open(path + file_name) as f:
            data = f.readlines()
        
        temp = {}
        for i in data:
            temp['record_id'] = zulip_record_id
            temp['orgnization'] = file_name[0:-4]
            if i[0:6] == '发送者姓名：':
                send_user_name = i.strip()[6:]
                temp['send_user_name'] = send_user_name
            elif i[0:6] == '发送者邮箱：':
                send_user_email = i.strip()[6:]
                temp['send_user_email'] = send_user_email
            elif i[0:3] == '时间：':
                send_time = i.strip()[3:]
                temp['send_time'] = send_time
            elif i[0:3] == '主题：':
                topic = i.strip()[3:]
                temp['topic'] = topic 
            elif i[0:3] == '内容：':
                content = i.strip()[3:]
                temp['content'] = content
            else:
                zulip_record_id += 1
                if 'content' in temp.keys():
                    dict_list.append(temp)
                temp = {}
                continue
    
    json.dump(dict_list, f_w)



if __name__ == '__main__':
    #to_csv('./complete/')
    to_dict('./complete/')
