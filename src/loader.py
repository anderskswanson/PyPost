from os.path import join
from yaml import load


class LoaderException(Exception):
    pass


class Loader:
    FILE_NOT_FOUND_ERR = 'File not found'
    INVALID_YAML_ERR = 'Failed to parse input yaml'

    @classmethod
    def get_yaml(cls, file):
        content = {}
        file = join(file)
        try:
            with open(file) as yamlfile:
                content = load(yamlfile)
        except FileNotFoundError as e:
            raise LoaderException(cls.FILE_NOT_FOUND_ERR, e)
        except Exception as e:
            raise LoaderException(cls.INVALID_YAML_ERR, e)
        return content
