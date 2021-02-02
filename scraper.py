import json
import random
import requests
import time
import os
import multiprocessing


class scraper:
    
    def __init__(self, token_list, proxies_ip_list):
      self.token_list = token_list
      self.proxies_ip_list = proxies_ip_list
      self.user_agent_list = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"]

    def requests_with_header_and_proxies(self, url):
        #[header_token, cookies_info] = random.choice(self.token_list).split(':')
        header_token = self.token_list[-1].split(':')[-1]
        #header_token = random.choice(self.token_list).split(':')[-1]
        user_agent = random.choice(self.user_agent_list)
        headers = {
            #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            #'Accept-Encoding': 'gzip, deflate, br',
            #'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            #'Cache-Control': 'max-age=0',
            #'Connection': 'keep-alive',
            #'Cookie': '_octo=GH1.1.223445760.1608802174; logged_in=yes; dotcom_user=CAKGOD; tz=Asia%2FShanghai',
            #'Host': 'api.github.com',
            #'Sec-Fetch-Dest': 'document',
            #'Sec-Fetch-Mode': 'navigate',
            #'Sec-Fetch-Site': 'none',
            #'Sec-Fetch-User': '?1',
            #'Upgrade-Insecure-Requests': '1',
            'user-Agent': user_agent,
            'Authorization': 'token ' + header_token
        }
        proxies = {'http': random.choice(self.proxies_ip_list)}
        #response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
        #response = requests.get(url, headers=headers, proxies=proxies)
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f'Response from {url} error.', response.status_code)
            return

        print(f'Response from {url} succeed.')

        return response


    def save_reponse_to_json(self, response, path):
        with open(path, 'w') as f:
            json.dump(json.loads(response.text), f)


    def download_common(self, url, path):
        self.save_reponse_to_json(self.requests_with_header_and_proxies(url), path)


    def multi_process_download(self, task, map_list, process_num):
        pool = multiprocessing.Pool(process_num)
        pool.map(task, map_list)
        pool.close()
        pool.join()


    def if_file_is_downloaded(self, file_name, search_item):
        with open(file_name) as f:
            data = [i.strip() for i in f.readlines()]
        if search_item in data:
            print(f'{search_item} is already downloaded.')
            return True
        return False


    def wirte_downloaded_item_to_file(self, file_name, write_item):
        with open(file_name, 'a') as f:
            f.write(write_item + '\n')


    def download_github_user_basic_info(self, user_login, path):
        url = 'https://api.github.com/users/' + user_login
        self.save_reponse_to_json(self.requests_with_header_and_proxies(url), path)


    def download_github_user_followers_info(self, user_login, path):
        url = 'https://api.github.com/users/' + user_login + '/following'
        self.save_reponse_to_json(self.requests_with_header_and_proxies(url), path)


    def download_github_orgnization_basic_info(self, org_login, path):
        url = 'https://api.github.com/orgs/' + org_login
        self.save_reponse_to_json(self.requests_with_header_and_proxies(url), path)


    def download_crates_io_basic_info(self, crate_id):
        if self.if_file_is_downloaded('/home/cakgod/myfile/myCode/data/crate/label/basic_crate_name.txt', crate_id):
            return
        url = 'https://crates.io/api/v1/crates/' + crate_id
        path = '/home/cakgod/myfile/myCode/data/crate/basic/' + crate_id + '_self.json'
        self.save_reponse_to_json(self.requests_with_header_and_proxies(url), path)
        self.wirte_downloaded_item_to_file('/home/cakgod/myfile/myCode/data/crate/label/basic_crate_name.txt', crate_id)


    def download_crates_io_owners_info(self, crate_id, path):
        url = 'https://crates.io/api/v1/crates/' + crate_id + '/owners'
        self.save_reponse_to_json(self.requests_with_header_and_proxies(url), path)


    def download_crates_io_authors_info(self, crate_id, crate_version, path):
        url = 'https://crates.io/api/v1/crates/' + crate_id + '/' + crate_version + '/authors'
        self.save_reponse_to_json(self.requests_with_header_and_proxies(url), path)


    def download_crates_io_dependencies_info(self, crate_id, crate_version, path):
        url = 'https://crates.io/api/v1/crates/' + crate_id + '/' + crate_version + '/dependencies'
        self.save_reponse_to_json(self.requests_with_header_and_proxies(url), path)


    def download_url_commit_basic_info(self, url, basic_label_path, save_path):
        crate_org_id = url.split('https://github.com/')[-1] 
        page_num = 1
        while (page_num):
            url_with_page_num = 'https://api.github.com/repos/' + crate_org_id + '/commits?page=' + str(page_num)
            print(url_with_page_num)
            if self.if_file_is_downloaded(basic_label_path, url_with_page_num):
                page_num += 1
                continue
            print(f'begin downloading {url_with_page_num}.')
            try:
                commit_response = self.requests_with_header_and_proxies(url_with_page_num)
            except:
                break
            if len(json.loads(commit_response.text)) == 0:
                break
            self.save_reponse_to_json(commit_response, save_path + crate_org_id.replace('/', '&') + '#' + str(page_num) + '.json')
            #self.download_common(url_with_page_num, save_path + crate_org_id.replace('/', '&') + '#' + str(page_num) + '.json')
            self.wirte_downloaded_item_to_file(basic_label_path, url_with_page_num)
            page_num += 1
            time.sleep(random.randint(1, 3))


    def download_url_commit_spec_info(self, basic_commits_path, spec_label_path, save_path):
        with open('../data/crate/commits/basic/' + basic_commits_path) as f:
            basic_commits_data = json.loads(f.readline())
        for i in basic_commits_data:
            spec_commit_url = i['url']
            if self.if_file_is_downloaded(spec_label_path, spec_commit_url):
                continue
            print(f'begin downloading {spec_commit_url}')
            self.download_common(spec_commit_url, save_path + basic_commits_path.split('#')[0] + '@' + i['sha'] + '.json')
            self.wirte_downloaded_item_to_file(spec_label_path, spec_commit_url)


    def extract_crates_author_info(self, crate_names):
        result = []
        for i in crate_names:
            crate_dict = {}
            # basic
            basic_path = '../data/crate/basic/' + i + '_self.json'
            temp_dict = json.loads(open(basic_path).readline())
            crate_dict.setdefault('id', '')
            crate_dict['id'] = temp_dict['crate']['id']
            crate_dict.setdefault('name', '')
            crate_dict['name'] = temp_dict['crate']['name']
            crate_dict.setdefault('crated_at', '')
            crate_dict['crated_at'] = temp_dict['crate']['created_at']
            crate_dict.setdefault('updated_at', '')
            crate_dict['updated_at'] = temp_dict['crate']['updated_at']
            crate_dict.setdefault('keywords', '')
            crate_dict['keywords'] = ','.join(temp_dict['crate']['keywords'])
            crate_dict.setdefault('categories', '')
            crate_dict['categories'] = ','.join(temp_dict['crate']['categories'])
            crate_dict.setdefault('downloads', 0)
            crate_dict['downloads'] = temp_dict['crate']['downloads']
            crate_dict.setdefault('recent_downloads', 0)
            crate_dict['recent_downloads'] = temp_dict['crate']['recent_downloads']
            crate_dict.setdefault('description', '')
            crate_dict['description'] = temp_dict['crate']['description']
            crate_dict.setdefault('homepage', '')
            crate_dict['homepage'] = temp_dict['crate']['homepage']
            crate_dict.setdefault('documentation', '')
            crate_dict['documentation'] = temp_dict['crate']['documentation']
            crate_dict.setdefault('repository', '')
            crate_dict['repository'] = temp_dict['crate']['repository']
            
            # owners
            owners_path = '../data/crate/owners/' + i + '_owners.json'
            temp_dict = json.loads(open(owners_path).readline())
            crate_dict.setdefault('owners', [])
            crate_dict['owners'] = list(temp_dict.values())[0]

            # authors
            authors_path = '../data/crate/authors/' + i + '_authors.json'
            temp_dict = json.loads(open(authors_path).readline())
            crate_dict.setdefault('authors', [])
            try:
                crate_dict['authors'] = temp_dict['meta']['names']
            except:
                print(f'{i} has no authors.')

            # dependencies
            dependencies_path = '../data/crate/dependencies/' + i + '_dependencies.json'
            temp_dict = json.loads(open(dependencies_path).readline())
            #crate_dict.setdefault('dependencies_path', [])
            try:
                dependencies_list = temp_dict['dependencies']
                for i in dependencies_list:
                    crate_dict.setdefault('normal_dependencies', [])
                    crate_dict.setdefault('normal_optional_dependencies', [])
                    crate_dict.setdefault('dev_dependencies', [])
                    crate_dict.setdefault('dev_optional_dependencies', [])
                    crate_dict.setdefault('build_dependencies', [])
                    crate_dict.setdefault('build_optional_dependencies', [])
                    if i['kind'] == 'normal' and i['optional'] == False:
                        crate_dict['normal_dependencies'].append(i['crate_id'])
                    elif i['kind'] == 'normal' and i['optional'] == True:
                        crate_dict['normal_optional_dependencies'].append(i['crate_id'])
                    elif i['kind'] == 'dev' and i['optional'] == False:
                        crate_dict['dev_dependencies'].append(i['crate_id'])
                    elif i['kind'] == 'dev' and i['optional'] == True:
                        crate_dict['dev_optional_dependencies'].append(i['crate_id'])
                    elif i['kind'] == 'build' and i['optional'] == False:
                        crate_dict['build_dependencies'].append(i['crate_id'])
                    else:
                        crate_dict['build_optional_dependencies'].append(i['crate_id'])
            
            except:
                print(f'{i} has no dependencies.')
            
            result.append(crate_dict)
        return result


    def extract_url_commit_spec_info(self, url_commit_dict, file_list):
        for i in file_list:
            if '@' not in i:
                continue
            dict_key = 'https://github.com/' + i.split('@')[0].replace('&', '/')
            if dict_key not in url_commit_dict.keys():
                url_commit_dict[dict_key] = {}
            with open(i) as f:
                data = json.loads(f.readline())
            committer = data['committer']['login']
            file_name_list = data['files']
            for j in file_name_list:
                file_name = j['filename']
                k_list = file_name.split('/')
                add_code_num = j['additions']
                delete_code_num = j['deletions']
                change_code_num = j['changes']
                for k in range(len(k_list) - 1):
                    k_list[k] += '/'
                new_file_name = ''
                for k in k_list:
                    new_file_name += k
                    if new_file_name not in url_commit_dict[dict_key].keys():
                        url_commit_dict[dict_key][new_file_name] = {}
                    if committer not in url_commit_dict[dict_key][new_file_name].keys():
                        url_commit_dict[dict_key][new_file_name][committer] = add_code_num
                    url_commit_dict[dict_key][new_file_name][committer] += add_code_num
        for k_0, v_0 in url_commit_dict.items():
            for k_1, v_1 in v_0.items():
                v_2 = sorted(v1.items(), key=lambda s:s[1], reverse=True)
                v_0[k_1] = v_2
        return url_commit_dict


    def download_projects_of_orgnization(self, org_login):
        repo_api = 'https://api.github.com/orgs/' + org_login + '/repos'
        response_content = self.requests_with_header_and_proxies(repo_api).text
        for i in json.loads(response_content):
            clone_url = i['clone_url']
            repo_name = clone_url.split('/')[-1].split('.')[0]
            print(f'git clone {clone_url} ...')
            os.system('git clone ' + clone_url + ' ../other/' + repo_name)


    def get_commit_log_file(self, path):
        os.system('git --no-pager log --stat >> commit_file.txt')


    def extract_commit_spec_info(self, path, file_commit_dict):
        with open('./commit_file.txt') as f:
            data = f.readlines()
        for i in data:
            if i.strip() == '' or i[0:2] == '  ' or i.strip().split(' ')[0] in ['commit', 'Merge:', 'Date:']:
                continue
            if i.strip().split(' ')[0] == 'Author:':
                author_name = i.strip().split(' ')[1].split('<')[0].strip()
            if i[0] == ' ' and '|' in i:
                useful_thing = i.strip().split(' ')
                add_num = useful_thing[-1].count('+')
                file_name_split = useful_thing[0].split('/')
                for j in range(len(file_name_list)-1):
                    file_name_list[j] += '/'
                file_name = ''
                for j in file_name_list:
                    file_name += j
                    if file_name not in file_commit_dict.keys():
                        file_commit_dict[file_name] = {}
                    if author_name not in file_commit_dict[file_name].keys():
                        file_commit_dict[file_name][author_name] = add_num
                    file_commit_dict[file_name][author_name] += add_num
        return file_commit_dict


    def download_all_user_following_info(self, user_logins):
        if type(user_logins) == list:
            for i in user_logins:
                if self.if_file_is_downloaded('../data/author/label/following_label.txt', i):
                    continue
                self.download_github_user_followers_info(i, '../data/author/following/' + i + '_following.json')
                self.wirte_downloaded_item_to_file('../data/author/label/following_label.txt', i)
                print(f'the following info of {i} has been downloaded')
        else:
            if self.if_file_is_downloaded('../data/author/label/following_label.txt', i):
                return
            self.download_github_user_followers_info(user_logins, '../data/author/following/' + user_logins + '_following.json')
            self.wirte_downloaded_item_to_file('../data/author/label/following_label.txt', user_logins)
            print(f'the following info of {i} has been downloaded')
        time.sleep(random.randint(1, 3))
