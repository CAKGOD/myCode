from scraper import scraper
from file_tool import file_tool
from rust_tool import rust_tool
from knowledge_graph import knowledge_graph 

if __name__ == '__main__':
    
    # set some default values of scraper
    srp = scraper(['shanchenqi:3c0709d2bb84222f0fb8ff1fc559420d566b4df4',
                   'sunbo57123:755f2fef6f366bc313d7781ed1d2583a25d28f97',
                   'CAKGOD:14e9ca9f60869cc4e885a7dc252bae838d803e4e'],
                  ['36.33.20.38:4226',
                   '182.132.103.182:4245',
                   '124.161.43.101:4258',
                   '114.238.38.54:4217',
                   '27.150.85.21:4284',
                   '124.112.4.186:4234',
                   '60.169.94.10:4278',
                   '117.63.135.61:4276',
                   '117.57.22.235:4278',
                   '112.123.40.239:4270'])
    # set some default values of file tool
    ft = file_tool('../data/author/basic/')

    # set some default values of rust tool
    #rt = rust_tool('./other/thanks')

    # set some default values of knowledge graph
    kg = knowledge_graph()

    # download crates basic info
    with open('../data/crate/label/all_crate_name.txt') as f1:
        crate_names = [i.strip() for i in f1.readlines()]
    #with open('../data/crate/label/basic_crate_name.txt') as f2:
    #    already_download_crate_names = [i.strip() for i in f2.readlines()]
    #download_goal = [i for i in crate_names if i not in already_download_crate_names]
    #srp.multi_process_download(srp.download_crates_io_basic_info, download_goal, 16)

    # extract crate info
    #crate_list = srp.extract_crates_author_info(crate_names)
    #print(crate_list[1000])

    #with open('./crate_list.json', 'w') as f:
    #    import json
    #    json.dump(crate_list, f)

    # download basic commit
    #with open('../data/crate/commits/basic/download_goal.txt') as f:
    #    basic_commit_url_list = [i.strip() for i in f.readlines()]
    #for i in basic_commit_url_list:
    #    srp.download_url_commit_basic_info(i, '../data/crate/commits/basic/download_label.txt', '../data/crate/commits/basic/')

    # download specific commit
    #for i in ft.get_all_current_files_name():
    #    if '#' in i:
    #        srp.download_url_commit_spec_info(i, '../data/crate/commits/spec/download_label.txt', '../data/crate/commits/spec/')

    # git clone 
    #srp.download_projects_of_orgnization('rust-lang')

    # extract commit
    #url_commit_dict = {}
    #file_list = ft.get_all_current_files_name()
    #self.extract_url_commit_spec_info(url_commit_dict, file_list)

    # download following of users
    #authors = [i.split('_api')[0] for i in ft.get_all_current_files_name()]
    #srp.download_all_user_following_info(authors)
    #srp.multi_process_download(srp.download_temp, authors, 16)

    # extract user info and construct Graph
    authors = [i.split('_api')[0] for i in ft.get_all_current_files_name()]
    user_info_dict, user_following_relation_dict = kg.extract_user_info_relations(authors)
    print(user_info_dict['KodrAus'])
    print(user_following_relation_dict['KodrAus'])
    import json
    json.dump(user_info_dict, open('../data/知识图谱数据/rust_user_info.json', 'w'))
    json.dump(user_following_relation_dict, open('../data/知识图谱数据/rust_following_relation.json', 'w'))

    #kg.construct_user_graph(kg.extract_user_info_relations(authors)[0], kg.extract_user_info_relations(authors)[1])
    #kg.save_graph()
