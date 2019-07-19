from jinja2 import Environment, FileSystemLoader
from os.path import join
from src.loader import Loader


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
                    lstrip_blocks=True),
                    yaml_loader=Loader):

        self._environment = environment
        self._loader = yaml_loader

    def substitute(self, subs, source):
        '''
        Substitute values from source into dest
        throws LoaderException, SubtitutionException
        '''
        substitutions = self._loader.from_file(subs)
        temp = self._environment.get_template(source)
        return self._loader.from_string(temp.render(substitutions))
