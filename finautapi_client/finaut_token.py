from __future__ import print_function
import urllib
import requests

PROTOCOL = 'http'
SERVER = 'localhost:8000'
FINAUTAPI = "{}://{}/finautapi/v1/".format(PROTOCOL, SERVER)

CLIENT_ID = 'xsojCstayZtM1VFx2zZd3Nq8JdsNXhP091A2GTKe'
CLIENT_SECRET = 'nRo351z8wiTWbDSscXCdfItEBiSEZunkyjQ5Q6AotA5pl2Zqv6ggoQNtIlot9yZItT7gzD2BxjlaqCpMHXSsUoWRr618ZvuUjC0PWb9bQVHNkVgyXTuj112iOf3x1S5s'

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
    url = FINAUTAPI + 'token/'
    payload = urllib.urlencode(dict(
        grant_type='client_credentials',
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scope=scope,
    ))
    response = requests.request("POST", url, headers=HEADERS, data=payload)
    print(response.text)
    return response.json()


def get_users(token):
    url = FINAUTAPI + "user/"
    response = requests.request("GET", url, headers={
        'Authorization': 'Bearer {}'.format(token),
        'Content-Type': 'application/x-www-form-urlencoded',
    }, data=urllib.urlencode(dict(
        username='bjorn'
    )))
    return response.text.encode('u8')


def get_groups(token):
    url = FINAUTAPI + "groups/"
    response = requests.request("GET", url, headers={
        'Authorization': 'Bearer {}'.format(token)
    })
    return response.text.encode('u8')


def xget_companies(token):
    url = FINAUTAPI + "comps/"
    response = requests.request("GET", url, headers={
        'Authorization': 'Bearer {}'.format(token)
    })
    return response.text.encode('u8')


def get_companies(token):
    url = FINAUTAPI + "companies/"
    response = requests.request("GET", url, headers={
        'Authorization': 'Bearer {}'.format(token)
    })
    return response.text.encode('u8')


def get_ordninger(token):
    url = FINAUTAPI + "ordninger/"
    print("URL:", url)
    response = requests.request("GET", url, headers={
        'Authorization': 'Bearer {}'.format(token)
    })
    print(response.status_code)
    return response.text.encode('u8')


def get_ordlist(token):
    url = FINAUTAPI + "ordlist/"
    print("URL:", url)
    response = requests.request("GET", url, headers={
        'Authorization': 'Bearer {}'.format(token)
    })
    return response.text.encode('u8')


def get_index(token):
    url = FINAUTAPI
    response = requests.request("GET", url, headers={
        'Authorization': 'Bearer {}'.format(token)
    })
    return response.text.encode('u8')




def get_secret(token):
    url = FINAUTAPI + 'secret/'
    response = requests.request("GET", url, headers={
        'Authorization': 'Bearer {}'.format(token)
    })
    return response.text.encode('u8')



if __name__ == "__main__":
    import json



    t = get_access_token("read")
    access_token = t['access_token']
    print()
    
    print(get_index(access_token))
    print(get_secret(access_token))
    print(json.dumps(json.loads(get_users(access_token)), indent=4))
    import sys
    sys.exit()


    # t = get_ordninger(access_token)
    t = get_companies(access_token)
    print(json.dumps(json.loads(t), indent=4))

    # t = get_ordlist(access_token)
    t = get_ordninger(access_token)
    print(json.dumps(json.loads(t), indent=4))
