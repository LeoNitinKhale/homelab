"""Operational data — ephemeral tasks and review state (ops DB).

Routed to the 'ops' database by config.db_router.OpsRouter. Models here must NOT
declare ForeignKeys to core apps (cross-database FKs are impossible); reference
core records by plain id instead (see related_kind / related_id).
"""

from common.models import TimestampedModel
from django.db import models


class Task(TimestampedModel):
    """A lightweight to-do / operational item. May loosely reference a core
    record (e.g. a trade to review) by kind + id, never by ForeignKey."""

    class Status(models.TextChoices):
        OPEN = 'open', 'Open'
        DONE = 'done', 'Done'

    title = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.OPEN)
    due_on = models.DateField(null=True, blank=True)

    # Loose, cross-database reference to a core record — plain strings/ids, no FK.
    related_kind = models.CharField(max_length=50, blank=True)   # e.g. 'trading.trade'
    related_id = models.PositiveBigIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['status', 'due_on', '-created_at']

    def __str__(self):
        return f'[{self.status}] {self.title}'
