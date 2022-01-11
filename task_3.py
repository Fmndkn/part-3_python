from pprint import pprint
from connections import Connections
import datetime
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
    
    def _get_response(self, uri, headers, params):
        response = requests.get(url=uri, headers=headers, params=params)
        return response.json()
    
    def get_response(self, uri, headers=None, params=None):
        return self._get_response(uri, headers, params)


def set_date_delta(day: int):
    now_date = datetime.datetime.now()
    delta = datetime.timedelta(days=day)
    return now_date + delta

def convert_date_unix(date):
    dt = datetime.datetime.fromisoformat(date)
    return dt.timestamp()


def set_date_for_params(delta_day: int, convert=True):
    if delta_day > 0 or delta_day < 0:
        date = datetime.datetime.now() - datetime.timedelta(days=delta_day)
    else:
        date = datetime.datetime.now()
        
    if convert == True:
        return convert_date_unix(str(date))
    else:
        return date


if __name__ == '__main__':

    name_connect = "stackoverflow"
    params = {
        "fromdate": int(set_date_for_params(-2)),
        "order": "asc",
        "sort": "hot",
        "tagged": "python",
        "site": "stackoverflow"
    }
    urn = ["2.3/questions"]
    
    connect_python = Connections(name=name_connect)
    req_python = RequestMain(connect_python, Connections)
    url = req_python.set_url_for_request(req_python.connect.url, urn)
    response = req_python.get_response(uri=url, params=params)
    
    pprint(response)