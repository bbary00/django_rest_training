import requests
import json
import os


END_POINT = 'http://localhost:8000/api/status/'
AUTH_ENDPOINT = 'http://localhost:8000/api/auth/'
REFRESH_ENDPOINT = 'http://localhost:8000/api/auth/jwt/refresh/'
image = os.path.join(os.getcwd(), 'grid-ai.jpg')


def do_img(method='get', data={}, is_json=True, img_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    if img_path:
        with open(img_path, 'rb') as img:
            file_data = {'image': img}
            r = requests.request(method, END_POINT, data=data, files=file_data, headers=headers)
    else:
        r = requests.request(method, END_POINT, data=data, headers=headers)
    return r.text


def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, END_POINT, data=data, headers=headers)
    return r.text


# print(do(method='put', data={'id': 3, 'content': 'This must be changed!'}))
# print(do(method='delete', data={'id': 300}))
# print(do(method='post', data={'user': 1, 'content': 'This is created right now!'}))
# print(do_img(method='post', data={'user': 1}, is_json=False, img_path=image))
# print(do())


post_headers = {
    'content-type': 'application/json'
}

# get_data_endpoint = END_POINT + str(17)
# r = requests.get(get_data_endpoint)
# print(r.text)
#
#
# post_data = json.dumps({'content': 'Here is test content'})
# r = requests.post(END_POINT, data=post_data, headers=post_headers)
# print(r.text)


# Login in and post data
# data = {'username': 'admin',
#         'password': 'admin'}
# r = requests.post(AUTH_ENDPOINT, headers=post_headers, data=json.dumps(data))
# token = r.json()['token']
#
#
# headers = {
#     'content-type': 'application/json',
#     'Authorization': 'JWT ' + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6Ik9yZXN0IiwiZXhwIjoxNTcxNDk0Mzk0LCJlbWFpbCI6Im9yZXN0QGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTcxNDk0MDk0fQ.bHTypX90DclMpgAWjeuZzfi-uwFlDkOChX4bQ3emjus"
# }
# with open(image, 'rb') as img:
#     file_data = {'image': img}
#     json_data = json.dumps({'content': 'Content with auth JWT token and image'})
#     data = {'content': 'Content with auth JWT token and image'}
#     r = requests.post(END_POINT, data=data, headers=headers, files=file_data)
#     print(r.text)


# Login in
# data = json.dumps({'username': 'Orest',
#                    'password': 'admin'})
# r = requests.post(AUTH_ENDPOINT, data=data, headers=headers)
# print(r.text)


# Perform registration
# data = json.dumps({'username': 'Orest10',
#                    'email': 'orest10@gmail.com',
#                    'password': 'admin',
#                    'password_confirmation': 'admin'})
#
# r = requests.post(AUTH_ENDPOINT + 'register/', data=data, headers=headers)
# print(r.text)


# Update status by user owner
login_data = {'username': 'Orest',
        'password': 'admin'}
r = requests.post(AUTH_ENDPOINT, headers=post_headers, data=json.dumps(login_data))
token = r.json()['token']
headers = {
    #'content-type': 'application/json',
    'Authorization': 'JWT ' + token
}
update_data = {
    'content': 'Update object if owner'
}
with open(image, 'rb') as img:
    file_data = {'image': img}

    # Update obj
    # r = requests.put(END_POINT + str(24), data=update_data, headers=headers, files=file_data)
    # print(r.text)

    # Create obj
    r = requests.post(END_POINT, data=update_data, headers=headers, files=file_data)
    print(r.text)

    # Get list
    r = requests.get(END_POINT, headers=headers)
    print(r.text)

    # Get obj
    r = requests.get(END_POINT + str(24), headers=headers)
    print(r.text)

    # Delete obj
    r = requests.delete(END_POINT + str(24), headers=headers)
    print(r.text)














