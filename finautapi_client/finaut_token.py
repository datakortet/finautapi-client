from __future__ import print_function
import urllib
import requests

PROTOCOL = 'http'
SERVER = 'localhost:8000'
PATH_TOKEN = '/o/token/'
PATH_USERS = '/finautapi/v1/users/'
PATH_GROUPS = '/finautapi/v1/groups/'
PATH_COMPANIES = '/finautapi/v1/companies/'

CLIENT_ID = 'dhMqAs7Dd892Q0kS0PnGOs7HvcvfTCbvMtNLM11Y'
CLIENT_SECRET = 'BiQJHpaVvAgNtTZvzN19lpf6MnlpuOnhPtGsUl6UM4bDuKoetc4VpmzgUx00Vq1Dgp5NdOzsT4gI5CgneY0slO5oxrx8szrjD0OIaQLJ9J8OGyyNplUrQVtRPwT6tc0V'

HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

def get_access_token(scope):
    """Returns a bearer token of the form

       ::

            {
                "access_token": "2hM4bzHXGIIf97HduyWRv88XDngukc",
                "token_type": "Bearer",
                "expires_in": 36000,
                "scope": "read write company"
            }

    """
    url = "{}://{}{}".format(PROTOCOL, SERVER, PATH_TOKEN)
    payload = urllib.urlencode(dict(
        grant_type='client_credentials',
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scope=scope,
    ))
    response = requests.request("POST", url, headers=HEADERS, data=payload)
    print(response.text)
    return response.json()


# def get_users(token):
#     url = "{}://{}{}".format(PROTOCOL, SERVER, PATH_USERS)
#     response = requests.request("GET", url, headers={
#         'Authorization': 'Bearer {}'.format(token),
#         'Content-Type': 'application/x-www-form-urlencoded',
#     }, data=urllib.urlencode(dict(
#         username='bjorn'
#     )))
#     return response.text.encode('u8')


# def get_groups(token):
#     url = "{}://{}{}".format(PROTOCOL, SERVER, PATH_GROUPS)
#     response = requests.request("GET", url, headers={
#         'Authorization': 'Bearer {}'.format(token)
#     })
#     return response.text.encode('u8')


# def xget_companies(token):
#     url = "{}://{}{}".format(PROTOCOL, SERVER, PATH_COMPANIES)
#     response = requests.request("GET", url, headers={
#         'Authorization': 'Bearer {}'.format(token)
#     })
#     return response.text.encode('u8')


def get_companies(token):
    url = "http://localhost:8000/finautapi/v1/companies/"
    response = requests.request("GET", url, headers={
        'Authorization': 'Bearer {}'.format(token)
    })
    return response.text.encode('u8')




if __name__ == "__main__":
    import json
    # print(get_access_token("read"))
    print(get_companies('MZ0xb643NWVichCUSIjOIk99SsdpiW'))

    # t = get_access_token('users')
    # print(json.dumps(t, indent=4))
    # print(get_groups(t['access_token']))
