from unittest import TestCase
from src.loader import Loader, LoaderException


class TestLoader(TestCase):

    def test_load_invalid_yaml(self):
        pass

    def test_load_file_not_found(self):
        try:
            Loader.get_yaml('not a file')
        except LoaderException as e:
            self.assertEqual(Loader.FILE_NOT_FOUND_ERR, e.args[0])
        except Exception as e:
            self.fail('Raised exception {}'.format(e))
        else:
            self.fail('Expected {}'.format(LoaderException.__name__))