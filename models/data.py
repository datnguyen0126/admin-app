import requests, json
from .config import Configurations

url = Configurations.API_URL + 'data'
url_cluster = Configurations.API_URL + 'result/cluster_data'


def get_all_product(name=''):
    try:
        response = requests.get(url + f'?name={name}')
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
    except Exception:
        return


def get_product(id):
    try:
        response = requests.get(url + f'/{id}')
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
    except Exception:
        return


def update_product(id, form_data):
    try:
        response = requests.put(url + f'/{id}', data=form_data)
        if response.status_code == 200:
            print('update ok')
            data = json.loads(response.text)
            return data
    except Exception:
        return


def get_all_clustering_data():
    try:
        response = requests.get(url_cluster)
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
    except Exception:
        return


def get_clustering_data(laptop_id):
    try:
        response = requests.get(Configurations.API_URL + f'result/{laptop_id}/cluster_data_product')
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
    except Exception:
        return


def reload_score(laptop_id):
    try:
        response = requests.get(Configurations.API_URL + f'result/{laptop_id}/set_benchmark_product')
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
    except Exception:
        return


def set_train_products(laptop_ids, answer):
    try:
        form_data = {
            'ids': ' '.join([str(elem) for elem in laptop_ids]),
            'content': answer
        }
        response = requests.post(Configurations.API_URL + 'result/set_train_products', data=form_data)
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
    except Exception as e:
        print(e)
        return


def get_train_products(answer):
    try:
        form_data = {
            'content': answer
        }
        response = requests.post(Configurations.API_URL + 'result/get_train_products', data=form_data)
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
    except Exception as e:
        print(e)
        return


def remove_train_product(id, answer):
    try:
        form_data = {
            'laptop_id': id,
            'content': answer
        }
        response = requests.put(Configurations.API_URL + 'result/remove_train_product', data=form_data)
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
    except Exception as e:
        print(e)
        return

