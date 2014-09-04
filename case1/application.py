
import argparse

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key', type=str, required=True,
                         help='authentication key',)
    args = parser.parse_args()

    do_something(args.key)


if __name__ == '__main__':
    main()
