from pprint import pprint
from file_operations import FileOperations
from connections import Connections
#from request_main import RequestMain
import requests

class RequestMain():
    def __init__(self, subject, clsass):
        if isinstance(subject, clsass):
            self.name = subject.name
            self.connect = subject
        else:
            self.name = None
    
    def send_request(self, url, params={}, headers={}):
        data = {"result": True, "log": []}
        log_mess = "Ошибка запроса"
        response = requests.get(url=url, params=params, headers=headers)
        if response.status_code == 200:
            t_data = response.json()
            tmp_response = self.check_status_response(t_data)
            if not tmp_response == False:
                data['data'] = t_data['results']
                return data
            else:
                data['result'] = False
                data['log'].append(log_mess)
                data['status_code'] = response.status_code
        else:
            data['result'] = False
            data['log'].append(log_mess)
            data['status_code'] = response.status_code
        
        return data

    def check_status_response(self, data):
        if 'response' in data and data['response'] == 'success':
            return data
        else:
            return False

    @staticmethod
    def set_url_for_request(url, urn=[]):
        uri = ""
        if len(urn) > 0:
            urn = "/".join(urn)
            uri = f"{url}/{urn}"
        else:
            uri = url
        
        return uri

def check_subject_to_object(subject):
    if subject.name != None:
        return True
    else:
        return False

def get_list_hero(list_response, subject, api_urn):
    result = {}
    if check_subject_to_object(subject):
        for i in list_response:
            urn = [*api_urn, i]
            uri = subject.set_url_for_request(subject.connect.url, urn)
            result[i] = subject.send_request(uri)
    else:
        result = False

    return result

def get_strongest_hero(data, list_hero):
    result = {}
    for i in list_hero:
        for v in data[i]['data']:
            if v['name'] == i:
                result[i] = v['powerstats']['intelligence']
    return result

if __name__ == '__main__':
    
    name_connect = "superhero"
    list_task = ["Thanos", "Hulk", "Captain America"]

    connect_hero = Connections(name=name_connect)
    req_hero = RequestMain(connect_hero, Connections)
    response = get_list_hero(list_task, req_hero, ['search'])
    
    if not response == False:
        list_hero = get_strongest_hero(response, list_task)
        name = max(list_hero, key=lambda x: int(list_hero[x]))
        print(f"Самый сильный герой ==> {name}")
    else:
        print("Что-то пошло не так, нужно логи поднимать. Нет ответа.")