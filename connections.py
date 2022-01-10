import json
import os

class FileOperations:
    def is_file(path, mode='r'):
        try:
            f = open(path, mode)
            f.close()
        except IOError:
            return False

        return True

class Connections:
    def __init__():
        return True
    
    def __str__():
        string = f"Object established {self..__name__}"
    
    def open_settings(type="relative"):
        settings = {}
        

        return settings
    
    def open_json_file(path):
        ...
    
    def _set_patch(type, part_path, name):
        if type == 'absolute':
            path_open = os.path.join(os.getcwd(), part_path, name)
        elif type == 'relative':
            path_open = os.path.join(part_path, name)
        else:
            return False
        
        return path_open

e = Connections()
print(f"{e}")