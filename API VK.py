import requests

from urllib.parse import urlencode
#
#
# OAUTH = 'https://oauth.vk.com/authorize'
# params_dict = {
#     'client_id': 7507933,
#     'display_page': 'page',
#     'scope': 'friends',
#     'response_type': 'token',
#     'v' : 5.89
# }
#
# print('?'.join((OAUTH,urlencode(params_dict))))

TOKEN_VALUE = 'a24a09fc261c8a40333af5acbffafb5aae5dd077db3bf35d84ee1b52c997caa3dfbb2024001f5eab23b8c'

# params = {
#     'source_uid' : 12312,
#     'access_token': TOKEN_VALUE,
#     'target_uid': '261513637',
#     'v' :5.89
# }
#
# response = requests.get('https://api.vk.com/method/friends.getMutual',params)
#
# print(response.json()['response'])


class USERS_FRIENDS:
    def __init__(self,id = str ,token = str)-> None:
        self.token = token
        self.id = id
        self.v = 5.89

    def __and__(self, object):
        params = {
            'source_uid': self.id,
            'access_token': self.token,
            'target_uid': object.id,
            'v': 5.89
        }

        links = []

        response = requests.get('https://api.vk.com/method/friends.getMutual', params)

        ids = response.json()['response']
        for values in ids:
            links.append(USERS_FRIENDS(str(values),TOKEN_VALUE))



        return links

    def print(self):
        string = 'https://vk.com/id'
        print(string+self.id)

#begin

Oleg = USERS_FRIENDS('281813247',TOKEN_VALUE)
Artem = USERS_FRIENDS('261513637', TOKEN_VALUE)

for values in Oleg & Artem:
    values.print()