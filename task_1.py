from pprint import pprint
from file_operations import FileOperations
from connections import Connections
from request_main import RequestMain

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
    
    name_hero = "superhero"
    list_task = ["Thanos", "Hulk", "Captain America"]

    connect_hero = Connections(name=name_hero)
    req_hero = RequestMain(connect_hero, Connections)
    response = get_list_hero(list_task, req_hero, ['search'])
    
    if not response == False:
        list_hero = get_strongest_hero(response, list_task)
        name = max(list_hero, key=lambda x: int(list_hero[x]))
        print(f"Самый сильный герой ==> {name}")
    else:
        print("Что-то пошло не так, нужно логи поднимать. Нет ответа.")