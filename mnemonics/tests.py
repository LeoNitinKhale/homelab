from django.db import IntegrityError
from django.test import TestCase

from .models import Peg


class PegTests(TestCase):
    def test_peg_saves_and_stringifies(self):
        peg = Peg.objects.create(number=1, word='hat')
        self.assertEqual(str(peg), '1: hat')
        self.assertIsNotNone(peg.created_at)   # from TimestampedModel

    def test_number_is_unique(self):
        Peg.objects.create(number=1, word='hat')
        with self.assertRaises(IntegrityError):
            Peg.objects.create(number=1, word='hen')
