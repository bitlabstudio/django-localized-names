"""Models for testing purposes."""
from django.db import models


class DummyModel(models.Model):
    """A model for testing only."""
    title = models.CharField(max_length=64)
    romanized_first_name = models.CharField(max_length=64)
    romanized_last_name = models.CharField(max_length=64)
    non_romanized_first_name = models.CharField(max_length=64)
    non_romanized_last_name = models.CharField(max_length=64)
    nickname = models.CharField(max_length=64)

    def get_title(self):
        return self.title

    def get_romanized_first_name(self):
        return self.romanized_first_name

    def get_romanized_last_name(self):
        return self.romanized_last_name

    def get_non_romanized_first_name(self):
        return self.non_romanized_first_name

    def get_non_romanized_last_name(self):
        return self.non_romanized_last_name

    def get_nickname(self):
        return self.nickname
