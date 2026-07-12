"""Trading database — trades and performance (core DB).

Starter model only; positions, instruments and performance rollups follow.
"""

from decimal import Decimal

from common.models import TimestampedModel
from django.db import models


class Trade(TimestampedModel):
    """A single round-trip trade. Open while exit_price/closed_on are null."""

    class Direction(models.TextChoices):
        LONG = 'long', 'Long'
        SHORT = 'short', 'Short'

    symbol = models.CharField(max_length=20)
    direction = models.CharField(max_length=5, choices=Direction.choices, default=Direction.LONG)
    quantity = models.DecimalField(max_digits=18, decimal_places=4)
    entry_price = models.DecimalField(max_digits=18, decimal_places=4)
    exit_price = models.DecimalField(max_digits=18, decimal_places=4, null=True, blank=True)
    opened_on = models.DateField()
    closed_on = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-opened_on', '-created_at']

    def __str__(self):
        state = 'open' if self.is_open else 'closed'
        return f'{self.symbol} {self.direction} x{self.quantity} ({state})'

    @property
    def is_open(self):
        return self.exit_price is None

    @property
    def pnl(self):
        """Realised profit/loss, or None while the trade is still open.
        Long: (exit - entry) * qty. Short: (entry - exit) * qty."""
        if self.is_open:
            return None
        diff = self.exit_price - self.entry_price
        if self.direction == self.Direction.SHORT:
            diff = -diff
        return (diff * self.quantity).quantize(Decimal('0.0001'))
