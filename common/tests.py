from django.test import TestCase

from common.models import CreatedModel, TimestampedModel, UpdatedModel


class BaseModelTests(TestCase):
    """The bases are abstract — they must never create their own table."""

    def test_bases_are_abstract(self):
        self.assertTrue(CreatedModel._meta.abstract)
        self.assertTrue(UpdatedModel._meta.abstract)
        self.assertTrue(TimestampedModel._meta.abstract)

    def test_timestamped_provides_both_fields(self):
        field_names = {f.name for f in TimestampedModel._meta.get_fields()}
        self.assertIn('created_at', field_names)
        self.assertIn('updated_at', field_names)
