from unittest import TestCase
from unittest.mock import MagicMock
from requests import Response
from src.pypost_http import RequestWrapper, InvalidMethodError, http_methods, GET


class TestPyPostHttp(TestCase):

    def test_invalid_method(self):
        try:
            r = RequestWrapper('foo', 'bar')
        except InvalidMethodError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised: {}'.format(e))
        else:
            self.fail('Excepted exception: {}'
                      .format(InvalidMethodError.__name__))

    def test_send_request(self):
        url = 'https://foo.com'
        body = 'here is some data'
        http_methods[GET] = MagicMock(None)
        r = RequestWrapper(GET, url, data=body)
        r()
        http_methods[GET].assert_called_once_with(url, {'data': body})
