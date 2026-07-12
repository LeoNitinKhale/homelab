"""Mnemonic portal — memory pegs, images and phrases (core DB).

Starter model only; the full peg/image/phrase model lands as the portal grows.
"""

from common.models import TimestampedModel
from django.db import models


class Peg(TimestampedModel):
    """A single memory peg — a fixed number mapped to a memorable word/image,
    used as a hook to store and recall ordered information."""
    number = models.PositiveIntegerField(unique=True)
    word = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number}: {self.word}'
