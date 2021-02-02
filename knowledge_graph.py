import json as js
import networkx as nx
from networkx.readwrite import json_graph

class knowledge_graph():
    def __init__(self):
        self.user_graph = nx.DiGraph()
        self.project_graph = nx.DiGraph()


    def extract_user_info_relations(self, user_logins):
        user_info_dict = {}
        user_relation_dict = {}
        for i in user_logins:
            temp_dict = js.loads(open('../data/author/basic/' + i + '_api.json').readline())
            if i not in user_info_dict.keys():
                user_info_dict[i] = {'name': temp_dict['name'],
                                     'id': temp_dict['id'],
                                     'node_id': temp_dict['node_id'],
                                     'type': temp_dict['type'],
                                     'location': temp_dict['location'],
                                     'company': temp_dict['company'],
                                     'email': temp_dict['email'],
                                     'blog': temp_dict['blog'],
                                     'twitter_username': temp_dict['twitter_username'],
                                     'public_repos': temp_dict['public_repos'],
                                     'public_gists': temp_dict['public_gists'],
                                     'followers_num': temp_dict['followers'],
                                     'following_num': temp_dict['following'],
                                     'created_at': temp_dict['created_at'],
                                     'updated_at': temp_dict['updated_at'],
                                     'url': temp_dict['html_url'],
                                     'avatar_url': temp_dict['avatar_url']}
            temp_list = js.loads(open('../data/author/following/' + i + '_following.json').readline())
            if i not in user_relation_dict.keys():
                user_relation_dict[i] = []
                for j in temp_list:
                    user_relation_dict[i].append(j['login'])
        return user_info_dict, user_relation_dict


    def construct_user_graph(self, user_info_dict, user_relation_dict):
        for k, v in user_info_dict.items():
            self.user_graph.add_nodes_from([(k, v)])
        for k, v in user_relation_dict.items():
            for i in v:
                if i in self.user_graph.nodes():
                    self.user_graph.add_edges_from([(k, i, {'attribute': 'following'})])


    def save_graph(self):
        nx.write_yaml(self.user_graph, '../model/github_user_graph.yaml')


    def load_graph(self):
        nx.read_yaml('../model/github_user_graph.yaml')
