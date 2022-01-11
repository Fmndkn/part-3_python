from file_operations import FileOperations

class Connections:
    # Settings class so as not to commit the token
    # JSON file structure
    # {
    #     "key": {
    #         "name": "token",
    #          ...
    #     },
    #     "url": {
    #         "name": "url",
    #          ...
    #     }
    #     ...
    # }
    
    def __init__(self, name, file_name='settings.json', path_part='file', path_type='relative', individual=True):
        self.name = name
        self.path_type = path_type
        self.path_part = path_part
        self.file_name = file_name
        self.individual = individual
        self.location = "local"
        self.settings = {'result': True, 'log':[]}
        self.key_settings = ['key', 'url']
        self.open_settings()
    
    def __str__(self):
        name = type(self).__name__
        string = f"Class: {name}\nName: {self.name}"
        
        return string
    
    def open_settings(self):
        self.settings['path'] = FileOperations.set_path(self.path_part, self.file_name, self.path_type, self.location)
        self._pre_read_json()
        
        if self.settings['result'] == True:
            self._read_json_to_settings(self.settings['path'])
    
    def _pre_read_json(self):
        if self.settings['path'] == False or self.settings['path'] == None:
            self.settings['result'] = False
            log_mess = "Ошибка в параметрах. Настройки не загрузить." if self.settings['path'] == False else "Файл не существует. Настройки не загрузить."
            self.settings['log'].append(log_mess)
        # elif self.settings['path'] == None:
        #     self.settings['result'] = False
        #     self.settings['log'].append("Файл не существует. Настройки не загрузить.")
    
    def _read_json_to_settings(self, path):
        data = FileOperations.open_settings(path)
        for i in self.key_settings:
            if i in data:
                self._set_attr(i, data[i])
    
    def _set_attr(self, key, data):
        for n, v in data.items():
            if n == self.name:
                name = f"{key}" if self.individual == True else f"{key}_{n}"                
                setattr(self, name, v)