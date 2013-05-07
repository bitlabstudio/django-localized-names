"""
Factories for the models of the ``localized_names`` app and its ``test_app``.

"""
import factory

from .test_app.models import DummyModel


class DummyModelFactory(factory.Factory):
    """Factory for the ``DummyModel`` model."""
    FACTORY_FOR = DummyModel

    title = 'Mr.'
    romanized_first_name = factory.Sequence(
        lambda i: 'romanized_first_name{0}'.format(i))
    romanized_last_name = factory.Sequence(
        lambda i: 'romanized_last_name{0}'.format(i))
    non_romanized_first_name = factory.Sequence(
        lambda i: 'non_romanized_first_name{0}'.format(i))
    non_romanized_last_name = factory.Sequence(
        lambda i: 'non_romanized_last_name{0}'.format(i))
    nickname = factory.Sequence(lambda i: 'nickname{0}'.format(i))
