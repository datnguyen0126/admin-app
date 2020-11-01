import requests, json
from .config import Configurations

url = Configurations.API_URL + 'question'


def get_all_questions():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
    except Exception:
        return


def get_answer(id):
    try:
        response = requests.get(url + f'/{id}')
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
    except Exception:
        return


def post_answer(id, form_data):
    try:
        response = requests.post(url + f'/{id}', data=form_data)
        if response.status_code == 200:
            print('update ok')
            data = json.loads(response.text)
            return data
    except Exception:
        return


def update_answer(id, form_data):
    try:
        response = requests.put(url + f'/{id}', data=form_data)
        if response.status_code == 200:
            print('update ok')
            data = json.loads(response.text)
            return data
    except Exception:
        return
