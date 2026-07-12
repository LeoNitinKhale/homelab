from datetime import date
from decimal import Decimal

from django.test import TestCase

from .models import Trade


class TradePnlTests(TestCase):
    def test_open_trade_has_no_pnl(self):
        t = Trade.objects.create(
            symbol='AAPL', direction=Trade.Direction.LONG,
            quantity=Decimal('10'), entry_price=Decimal('100'), opened_on=date(2026, 1, 1),
        )
        self.assertTrue(t.is_open)
        self.assertIsNone(t.pnl)

    def test_long_pnl(self):
        t = Trade.objects.create(
            symbol='AAPL', direction=Trade.Direction.LONG,
            quantity=Decimal('10'), entry_price=Decimal('100'), exit_price=Decimal('110'),
            opened_on=date(2026, 1, 1), closed_on=date(2026, 1, 5),
        )
        self.assertFalse(t.is_open)
        self.assertEqual(t.pnl, Decimal('100.0000'))

    def test_short_pnl(self):
        t = Trade.objects.create(
            symbol='AAPL', direction=Trade.Direction.SHORT,
            quantity=Decimal('10'), entry_price=Decimal('100'), exit_price=Decimal('90'),
            opened_on=date(2026, 1, 1), closed_on=date(2026, 1, 5),
        )
        self.assertEqual(t.pnl, Decimal('100.0000'))

    def test_short_loss_is_negative(self):
        t = Trade.objects.create(
            symbol='AAPL', direction=Trade.Direction.SHORT,
            quantity=Decimal('10'), entry_price=Decimal('100'), exit_price=Decimal('110'),
            opened_on=date(2026, 1, 1), closed_on=date(2026, 1, 5),
        )
        self.assertEqual(t.pnl, Decimal('-100.0000'))
