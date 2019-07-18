import requests

GET = 'get'
HEAD = 'head'
POST = 'post'
PATCH = 'patch'
DELETE = 'delete'
OPTIONS = 'options'

http_methods = {
    GET: requests.get,
    HEAD: requests.head,
    POST: requests.post,
    PATCH: requests.patch,
    DELETE: requests.delete,
    OPTIONS: requests.options
}


class InvalidMethodError(Exception):
    pass


class RequestWrapper:
    def __init__(self, method, url, **params):
        if method not in http_methods:
            raise InvalidMethodError('Unknown http method')
        self._method = method
        self._url = url
        self._params = params

    def __call__(self):
        return http_methods[self._method](self._url, self._params)
