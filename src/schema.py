REQUESTS = 'requests'
METHOD = 'method'
URL = 'url'
ARGS = 'arguments'
DATA = 'data'
HEADERS = 'headers'


def get_req_data(req):
    return req[ARGS][DATA]


def get_req_headers(req):
    return req[ARGS][HEADERS]
