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

