import os

class file_tool():

    def __init__(self, path):
        self.path = path

    
    def get_current_path(self):
        for root, _, _ in os.walk(self.path):
            return root

    
    def get_all_current_sub_dir(self):
        for _, dirs, _ in os.walk(self.path):
            return dirs


    def get_all_current_files_name(self):
        for _, _, files in os.walk(self.path):
            return files


    def get_all_files_name(self, path, file_list):
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isdir(file_path):
                self.get_all_files_name(file_path, file_list)
            else:
                file_list.append(file_path)
    

    def write_fun(self, data, path):
        with open(path, 'a', 'utf8') as f:
            f.write(data + '\n')


    def read_fun(self, path):
        with open(path, encoding="utf8") as f:
            data = [i.strip() for i in f.readlines()]
        return data


