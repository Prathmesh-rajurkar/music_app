from rest_framework import serializers
from .models import * 


class RoomSerializer(serializers.Serializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')
