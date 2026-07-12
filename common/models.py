"""Abstract base models shared across the domain apps.

These are ABSTRACT — they create no table and no migration of their own. Each
concrete child (e.g. trading.Trade) gets its own copy of the columns in its own
table, so there is no shared table, no ForeignKey, and no cross-app/cross-DB
coupling. That is what lets ops (ops DB) and the core apps reuse the same bases.

Per CLAUDE.md: new models needing created/updated stamps must inherit these
rather than declaring the fields directly.
"""

from django.db import models


class CreatedModel(models.Model):
    """Adds an immutable creation timestamp. Use for append-only records."""
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedModel(models.Model):
    """Adds a last-modified timestamp."""
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TimestampedModel(CreatedModel, UpdatedModel):
    """Both created_at and updated_at — the default for anything mutable."""

    class Meta:
        abstract = True
