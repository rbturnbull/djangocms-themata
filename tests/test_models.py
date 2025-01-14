from django.test import TestCase

from djangocms_themata import models


class TestStylesheet(TestCase):
    def test_str(self):
        stylesheet = models.Stylesheet(name="Test")
        self.assertEqual(str(stylesheet), "Test")


    def test_fixture(self):
        assert models.Stylesheet.objects.count() > 10
        assert models.Stylesheet.objects.filter(active=True).count() == 1