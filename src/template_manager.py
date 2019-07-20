from jinja2 import Environment, FileSystemLoader
from os.path import join
from src.yaml_util import YamlUtil


class SubstitutionException(Exception):
    pass


class TemplateManager:
    '''
    Maintain the template environment and yaml loader
    Perform substitutions into templates inside the current environment
    '''
    def __init__(self, environment=Environment(
                    loader=FileSystemLoader(join('.')),
                    trim_blocks=True,
                    lstrip_blocks=True)):
        self._environment = environment

    def substitute(self, source, subs, format_fn=YamlUtil.from_string):
        '''
        Substitute values from source into dest
        throws LoaderException, SubtitutionException
        '''
        temp = self._environment.get_template(source)
        return format_fn(temp.render(subs))
