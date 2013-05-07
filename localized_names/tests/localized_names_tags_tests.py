"""Tests for the templatetags of the ``localized_names`` app."""
from django.conf import settings
from django.test import TestCase

from ..templatetags.localized_names_tags import get_name
from .factories import DummyModelFactory


class GetNameTestCase(TestCase):
    """Tests for the ``get_name`` templatetag."""
    longMessage = True

    def setUp(self):
        self.obj = DummyModelFactory()

    def test_get_name(self):
        """Test for the ``get_name`` templatetag."""
        setattr(settings, 'LONG_NAME_FORMAT', '{t} {f} "{n}" {l}')
        expected_output = '{} {} "{}" {}'.format(
            self.obj.title,
            self.obj.romanized_first_name,
            self.obj.nickname,
            self.obj.romanized_last_name,
        )
        self.assertEqual(
            get_name(self.obj, 'LONG_NAME_FORMAT'), expected_output, msg=(
                'Expected another value for the name format.'))

        setattr(settings, 'LONG_NAME_FORMAT', '{a}{x}{T} ({L}, "{N}", {F})')
        expected_output = '{}{}{} ({}, "{}", {})'.format(
            self.obj.non_romanized_first_name,
            self.obj.non_romanized_last_name,
            self.obj.title.upper(),
            self.obj.romanized_last_name.upper(),
            self.obj.nickname.upper(),
            self.obj.romanized_first_name.upper(),
        )
        self.assertEqual(
            get_name(self.obj), expected_output, msg=(
                'Expected another value for the name format.'))

        setattr(settings, 'SHORT_NAME_FORMAT', '{A}{X}')
        expected_output = '{}{}'.format(
            self.obj.non_romanized_first_name.upper(),
            self.obj.non_romanized_last_name.upper(),
        )
        self.assertEqual(
            get_name(self.obj, 'SHORT_NAME_FORMAT'), expected_output, msg=(
                'Expected another value for the name format.'))
