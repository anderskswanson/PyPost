from unittest import TestCase
from src.template_manager import TemplateManager
from src.yaml_util import YamlUtil


class TestTemplateManager(TestCase):

    def test_substitute_template(self):
        t = TemplateManager()
        expected = {'key': 'hello, world'}
        kvmap = YamlUtil.from_file('test/resources/simplesub.yaml')
        rendered = t.substitute('test/resources/simpletemplate.yaml', kvmap)
        self.assertEqual(expected, rendered)
