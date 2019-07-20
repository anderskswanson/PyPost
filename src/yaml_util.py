import os.path
from yaml import load, dump, FullLoader


class YamlException(Exception):
    pass


class YamlUtil:
    """Utility class for loading and dumping yaml"""

    FILE_NOT_FOUND_ERR = 'File not found'
    INVALID_YAML_ERR = 'Failed to parse input yaml'

    @classmethod
    def from_file(cls, file):
        """Get yaml object from a filepath
        file -- Path to a file containing yaml
        return -- yaml object
        """
        content = {}
        file = os.path.join(file)
        try:
            with open(file) as yamlfile:
                content = load(yamlfile)
        except FileNotFoundError as e:
            raise YamlException(cls.FILE_NOT_FOUND_ERR, e)
        except Exception as e:
            raise YamlException(cls.INVALID_YAML_ERR, e)
        return content

    @classmethod
    def to_file(cls, filepath, yaml_dict):
        """Convert yaml to file
        filepath -- path of file to render to
        yaml_dict -- yaml to render in file
        """
        with open(filepath, 'w') as out:
            dump(yaml_dict, out, default_flow_style=False)

    @classmethod
    def _stringify(cls, representation, yaml_fn):
        """Converter util
        representation -- object representing yaml
        yaml_fn -- function to convert representation
        return -- converted representation
        """
        content = None
        try:
            content = yaml_fn(representation)
        except Exception as e:
            raise YamlException(cls.INVALID_YAML_ERR, e)
        return content

    @classmethod
    def from_string(cls, string):
        """Convert string to yaml
        string -- string representation of yaml
        return -- yaml after conversion
        """
        return cls._stringify(string, load)

    @classmethod
    def to_string(cls, yaml_dict):
        """Convert yaml to string representation
        yaml_dict -- yaml to convert
        return -- string representation of yaml
        """
        return cls._stringify(yaml_dict, dump)
