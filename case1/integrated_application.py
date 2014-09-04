
import argparse
import requests
import json


# keys storage
KEYS = [
    'key1',
    'key2',
    'key3',
    'key4'
]


# action service prototype
def do_something(user_key):
    if is_permitted(user_key):
        print 'do something...'
    else:
        print 'unauthorized'


# auth service prototype
def is_permitted(user_key):
    return user_key in KEYS

# internall mapping between openstack user id and application key
MAPPING = {
    '569bcee6030e4306ba6aca58af75bc83': KEYS[2],
}


KEYSTONE_ENDPOINT = 'http://10.25.13.127:5000/v3/'


def get_openstack_user(name, password):
    url = KEYSTONE_ENDPOINT + 'auth/tokens/'
    auth = {
        'auth': {
            'identity': {
                'methods': ['password'],
                'password': {
                    'user': {
                        'name': name,
                        'domain': {'id': 'default'},
                        'password': password
                    }
                }
            }
        }
    }

    response = requests.post(url, data=json.dumps(auth))
    if response.status_code == 201:
        print 'openstack authorization done'
        result = response.json()
        return {
            'id': result.get('token').get('user').get('id'),
            'token': response.headers.get('x-subject-token'),
        }

    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', type=str, required=True,
                         help='OpenStack user name',)
    parser.add_argument('-p', '--password', type=str, required=True,
                         help='OpenStack user password',)
    args = parser.parse_args()

    user = get_openstack_user(args.username, args.password)
    user_key = MAPPING.get(user['id']) if user else None
    do_something(user_key)


if __name__ == '__main__':
    main()

