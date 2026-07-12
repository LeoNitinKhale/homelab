from rest_framework import serializers

from .models import Peg


class PegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peg
        fields = ['id', 'number', 'word', 'notes', 'created_at', 'updated_at']
