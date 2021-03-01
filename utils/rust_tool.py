class rust_tool():

    def __init__(self, index_project_path, thanks_path):
        # We need to clone the crates.io-index project from 'https://github.com/rust-lang/crates.io-index' firstly
        # and then set the path as the path of this project
        self.index_project_path = index_project_path
        self.thanks_path = thanks_path


    def get_all_crate_id(self):
        temp = []
        ft.get_all_files_name(self.index_project_path, temp)
        crate_id_list = [i.split('/')[-1] for i in temp]
        return crate_id_list


    def get_all_contributors_id(self):
        temp = []
