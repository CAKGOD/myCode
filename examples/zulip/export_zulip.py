#!/usr/bin/env python
# coding=utf-8

import zulip
import time
import re

client = zulip.Client(config_file="/home/cakgod/rust/rust_zulip/rc/zuliprc")

zulip_dict = {
    'core': ['wg-governance'],
    'language': ['t-lang', 't-lang/doc', 'project-ffi-unwind', 'project-inline-asm', 'project-safe-transmute', 't-lang/wg-unsafe-code-guidelines'],
    'library': ['t-libs'],
    'operation': ['t-infra'],
    'compiler': ['t-compiler', 't-compiler/wg-diagnostics', 't-compiler/wg-incr-comp', 't-compiler/wg-llvm', 't-compiler/wg-meta', 't-compiler/wg-mir-opt', 't-compiler/wg-nll', 't-compiler/wg-parallel-rustc', 't-compiler/wg-parselib', 't-compiler/wg-polonius', 't-compiler/wg-polymorphization', 't-compiler/wg-prioritization', 't-compiler/wg-rfc-2229', 't-compiler/wg-rls-2.0', 't-compiler/wg-rustc-dev-guide', 't-compiler/wg-self-profile', 'wg-traits'],
    'devTool': ['t-cargo', 'clippy'],
    # The devTool team contains some channels on Discord.
    # 'cratesIO': []
    # The cratesIO team contains some channels on Discord.
}

for i in zulip_dict.keys():
    temp_0 = []
    big_file_path = '../data/content/' + i + '.txt'

    f_b = open(big_file_path, 'a')

    for j in zulip_dict[i]:
        operand = j

        request = {
            'anchor': 'newest',
            'num_before': 5000,
            'num_after': 0,
            'narrow': [{'operator': 'stream', 'operand': operand}],
        }

        result = client.get_messages(request)
        
        j = j.replace('/', '_')
        small_file_path = '../data/complete/' + i + '_' + j + '.txt'
        
        with open(small_file_path) as f:
            data = f.readlines()
        label = -1
        while (label):
            if data[label][0] == '时':
                time_last = data[label].strip()[3:]
                time_stamp_last = int(time.mktime(time.strptime(time_last, "%Y--%m--%d %H:%M:%S")))
                break
            else:
                label -= 1
                continue

        f_s = open(small_file_path, 'a')

        for k in result['messages']:
            sender_name = k['sender_full_name']
            new_sender_name = '发送者姓名：' + sender_name + '\n'

            sender_email = k['sender_email']
            new_sender_email = '发送者邮箱：' + sender_email  + '\n'

            time_stamp = k['timestamp']
            time_array = time.localtime(time_stamp)
            new_time = '时间：' + time.strftime("%Y--%m--%d %H:%M:%S", time_array) + '\n'

            topic = k['subject']
            new_topic = '主题：' + topic  + '\n'

            content = k['content']
            pattern = re.compile(r'<[^>]+>', re.S)
            new_content = '内容：' + pattern.sub('', content) + '\n'

            if time_stamp <= time_stamp_last:
                continue

            f_s.write('**************************************************' + '\n')
            f_s.write(new_sender_name)
            f_s.write(new_sender_email)
            f_s.write(new_time)
            f_s.write(new_topic)
            f_s.write(new_content)
            f_b.write(new_content[3:])
        f_s.close()
    f_b.close()
