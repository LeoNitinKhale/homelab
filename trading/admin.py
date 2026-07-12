from django.contrib import admin

from .models import Trade


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'direction', 'quantity', 'entry_price', 'exit_price', 'pnl', 'opened_on')
    list_filter = ('direction', 'symbol')
    search_fields = ('symbol',)
    date_hierarchy = 'opened_on'
