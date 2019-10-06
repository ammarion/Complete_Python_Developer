# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True
}


def authenticated(fn):
    def auth_wrap(*args, **kwargs):
        if user1['valid']:
            return fn(*args, **kwargs)
    return auth_wrap


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
