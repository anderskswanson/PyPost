import httpretty
import re
import os.path
import src.schema
from unittest import TestCase
from unittest.mock import MagicMock
from requests import Response
from src.pypost_http import RequestWrapper, InvalidMethodError, http_methods, GET
from src.yaml_util import YamlUtil


class TestPyPostHttp(TestCase):

    @classmethod
    def setUp(self):
        self.wrapper = RequestWrapper()

    def test_invalid_method(self):
        try:
            self.wrapper(method='foo')
        except InvalidMethodError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised: {}'.format(e))
        else:
            self.fail('Excepted exception: {}'
                      .format(InvalidMethodError.__name__))

    def test_send_request(self):
        url = 'https://foo.com'
        body = 'here is a body'
        arg = {
            src.schema.METHOD: GET,
            src.schema.URL: url,
            src.schema.ARGS: {
                src.schema.DATA: body
            }
        }
        http_methods[GET] = MagicMock(None)
        self.wrapper(**arg)
        http_methods[GET].assert_called_once_with(url, **arg[src.schema.ARGS])

    def test_run_file_request(self):
        httpretty.enable()
        httpretty.register_uri(
            httpretty.GET,
            re.compile(r'http://.*'))

        data = YamlUtil.from_file(os.path.join(
            'test/resources/request.yaml'
        ))
        req = data['requests']['testrequest']
        body = src.schema.get_req_data(req)
        headers = src.schema.get_req_headers(req)
        self.wrapper(**req)
        resp = httpretty.last_request()
        self.assertEqual(req[src.schema.METHOD].lower(), resp.method.lower())
        self.assertEqual(body, resp.parsed_body)
        httpretty.disable()

        """
        requests:
  testrequest:
    method: 'get'
    url: 'http://foo.com'
    arguments:
      data: 'test body'
      headers:
        header1: 'this is a test header'
        header2: 'another test header'
        """