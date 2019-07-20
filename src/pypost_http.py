import requests
import src.schema

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
    def __call__(self, **req):
        method = req[src.schema.METHOD]
        if method not in http_methods:
            raise InvalidMethodError('Method {} not a valid http method'
                                     .format(method))
        url = req[src.schema.URL]
        arg = req[src.schema.ARGS]
        return http_methods[method](url, **arg)
