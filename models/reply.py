import requests, json
from .config import Configurations

url = Configurations.API_URL + 'result/reply'


def get_reply():
    try:
        response = requests.get(url + '/get')
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
    except Exception:
        return


def create_reply(form_data):
    try:
        response = requests.post(url + '/add', data=form_data)
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
    except Exception:
        return


def update_reply(id, form_data):
    try:
        response = requests.put(url + '/edit', data=form_data)
        if response.status_code == 200:
            print('update ok')
            data = json.loads(response.text)
            return data
    except Exception:
        return


def delete_reply(id):
    try:
        response = requests.delete(url + 'remove')
        if response.status_code == 200:
            print('update ok')
            data = json.loads(response.text)
            return data
    except Exception:
        return
