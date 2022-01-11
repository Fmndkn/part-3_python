from pprint import pprint
from file_operations import FileOperations
from connections import Connections
#from request_main import RequestMain

import requests

class RequestMain():
    def __init__(self, subject, class_subject):
        if isinstance(subject, class_subject):
            self.name = subject.name
            self.connect = subject
        else:
            self.name = None

    @staticmethod
    def set_url_for_request(url, urn=[]):
        uri = ""
        if len(urn) > 0:
            urn = "/".join(urn)
            uri = f"{url}/{urn}"
        else:
            uri = url
        
        return uri
    
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.connect.key)
        }
    
    def _get_response(self, uri, headers=None, params=None):
        response = requests.get(url=uri, headers=headers, params=params)
        return response.json()
        
    def get_files_list(self, urn):
        uri = self.set_url_for_request(self.connect.url, urn)
        headers = self.get_headers()
        response = self._get_response(uri, headers)
        
        return response

    def upload_files_to_yandex(self, uri_path_for_file, params_upload):
        urn_files = params_upload["remote_path"]
        path_file_local = FileOperations.set_path(
            params_upload["local_path"],
            params_upload["file_name"],
            "relative",
            "local"
        )
        params = {
            "path": urn_files,
            "overwrite": params_upload["overwrite"]
        }
        headers = self.get_headers()

        uri = self.set_url_for_request(self.connect.url, uri_path_for_file)
        uri = self._get_response(uri, headers=headers, params=params).get("href", "")
        response = requests.put(uri, data=open(path_file_local, 'rb'))
        response.raise_for_status()
        
        if response.status_code == 201:
            return True
        else:
            return False
        
if __name__ == '__main__':
    
    name_connect = "ya_disk"
    urn_list_path = ["v1/disk/resources/files"]
    urn_upload_path = ["v1/disk/resources/upload"]
    params_upload = {
        "remote_path": "Python_netology/test.txt",
        "local_path": "file",
        "file_name": "test.txt",
        "overwrite": "true"
    }

    connect_yadisk = Connections(name=name_connect, individual=True)
    request_yadisk = RequestMain(connect_yadisk, Connections)

    file_list = request_yadisk.get_files_list(urn_list_path)
    file_upload = request_yadisk.upload_files_to_yandex(urn_upload_path, params_upload)
    
    #pprint(file_list)
    #pprint(file_upload)