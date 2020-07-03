import requests
import json


URL = 'http://localhost:8000'

END_POINT = '/api/updates/'


def get_list():
    new_data = {
        'id': 11,
    }
    r = requests.get(URL + END_POINT, data=json.dumps(new_data))
    print(r.json())


def do_update():
    new_data = {
        'user': 1,
        'content': 'Some content',
    }

    r = requests.post(URL + END_POINT, data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        print(r.json())
    print(r.text)


def do_obj_update():
    new_data = {
        'content': 'Some another text',
        'id': 15,
    }

    r = requests.put(URL + END_POINT, data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        print(r.json())
    return r.text


def do_obj_delete():
    new_data = {
        'id': 16,
    }
    r = requests.delete(URL + END_POINT, data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        print(r.json())
    return r.text


# do_update()
# get_list()
# print(do_obj_update())
# print(do_obj_delete())
# do_obj_delete()
get_list()
