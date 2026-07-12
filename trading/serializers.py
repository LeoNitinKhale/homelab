from rest_framework import serializers

from .models import Trade


class TradeSerializer(serializers.ModelSerializer):
    # Computed model properties, exposed read-only.
    pnl = serializers.DecimalField(max_digits=18, decimal_places=4, read_only=True)
    is_open = serializers.BooleanField(read_only=True)

    class Meta:
        model = Trade
        fields = [
            'id', 'symbol', 'direction', 'quantity', 'entry_price', 'exit_price',
            'opened_on', 'closed_on', 'is_open', 'pnl', 'created_at', 'updated_at',
        ]
