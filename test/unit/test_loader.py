from unittest import TestCase
from src.loader import Loader, LoaderException


class TestLoader(TestCase):

    def test_load_invalid_yaml(self):
        try:
            Loader.from_file('test/resources/brokenyaml.yaml')
        except LoaderException as e:
            self.assertEqual(Loader.INVALID_YAML_ERR, e.args[0])
        except Exception as e:
            self.fail('Raised exception {}'.format(e))
        else:
            self.fail('Expected exception {}'.format(LoaderException.__name__))

    def test_load_file_not_found(self):
        try:
            Loader.from_file('not a file')
        except LoaderException as e:
            self.assertEqual(Loader.FILE_NOT_FOUND_ERR, e.args[0])
        except Exception as e:
            self.fail('Raised exception {}'.format(e))
        else:
            self.fail('Expected {}'.format(LoaderException.__name__))

    def test_load_valid_yaml(self):
        expected = {'key': 'value'}
        try:
            content = Loader.from_file('test/resources/simpleyaml.yaml')
        except Exception as e:
            self.fail()
        self.assertEqual(expected, content)

    def test_load_string(self):
        expected = {'key': 'value'}
        try:
            content = Loader.from_string("{'key': 'value'}")
        except Exception as e:
            self.fail()
        self.assertEqual(expected, content)

    def test_load_invalid_string(self):
        try:
            Loader.from_string("{a: b: c}")
        except LoaderException as e:
            self.assertEqual(Loader.INVALID_YAML_ERR, e.args[0])
        except Exception as e:
            self.fail()
        else:
            self.fail()
