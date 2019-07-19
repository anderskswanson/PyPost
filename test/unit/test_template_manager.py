from unittest import TestCase
from src.template_manager import TemplateManager


class TestTemplateManager(TestCase):

    def test_substitute_template(self):
        t = TemplateManager()
        expected = {'key': 'hello, world'}
        rendered = t.substitute('test/resources/simplesub.yaml',
                                'test/resources/simpletemplate.yaml')
        self.assertEqual(expected, rendered)
