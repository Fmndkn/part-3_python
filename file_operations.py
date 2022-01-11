import os
import json

class FileOperations:
    @staticmethod
    def is_file(path, mode='r'):
        try:
            f = open(path, mode)
            f.close()
        except IOError:
            return False
        return True
    
    def set_path(path_part, name, path_type, location):
        if path_type == 'absolute':
            path_open = os.path.join(os.getcwd(), path_part, name)
        elif path_type == 'relative':
            path_open = os.path.join(path_part, name)
        else:
            return False
        
        if location == "remote" or FileOperations.is_file(path_open):
            return path_open
        else:
            return None
        
    def open_settings(path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

