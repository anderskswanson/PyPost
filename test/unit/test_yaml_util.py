import os.path
from unittest import TestCase
from src.yaml_util import YamlUtil, YamlException


class TestLoader(TestCase):

    def test_load_invalid_yaml(self):
        try:
            YamlUtil.from_file('test/resources/brokenyaml.yaml')
        except YamlException as e:
            self.assertEqual(YamlUtil.INVALID_YAML_ERR, e.args[0])
        except Exception as e:
            self.fail('Raised exception {}'.format(e))
        else:
            self.fail('Expected exception {}'.format(YamlException.__name__))

    def test_load_file_not_found(self):
        try:
            YamlUtil.from_file('not a file')
        except YamlException as e:
            self.assertEqual(YamlUtil.FILE_NOT_FOUND_ERR, e.args[0])
        except Exception as e:
            self.fail('Raised exception {}'.format(e))
        else:
            self.fail('Expected {}'.format(YamlException.__name__))

    def test_load_valid_yaml(self):
        expected = {'key': 'value'}
        try:
            content = YamlUtil.from_file('test/resources/simpleyaml.yaml')
        except Exception as e:
            self.fail()
        self.assertEqual(expected, content)

    def test_load_string(self):
        expected = {'key': 'value'}
        try:
            content = YamlUtil.from_string("{'key': 'value'}")
        except Exception as e:
            self.fail()
        self.assertEqual(expected, content)

    def test_load_invalid_string(self):
        try:
            YamlUtil.from_string("{a: b: c}")
        except YamlException as e:
            self.assertEqual(YamlUtil.INVALID_YAML_ERR, e.args[0])
        except Exception as e:
            self.fail()
        else:
            self.fail()

    def test_to_file(self):
        tempfile = os.path.join('test/resources/tempfile.yaml')
        if os.path.exists(tempfile):
            os.remove(tempfile)

        output = YamlUtil.from_string('{key: value}')
        YamlUtil.to_file(tempfile, output)
        self.assertEqual(output, YamlUtil.from_file(tempfile))
        os.remove(tempfile)

    def test_to_string(self):
        stryaml = '{key: value}'
        converted = YamlUtil.from_string(stryaml)
        reverted = YamlUtil.to_string(converted)
        self.assertTrue('key' in reverted)
        self.assertTrue('value' in reverted)
